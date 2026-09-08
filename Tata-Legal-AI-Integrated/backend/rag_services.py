import os
import re
from pathlib import Path
from typing import List, Dict, Any

import chromadb
from dotenv import load_dotenv

load_dotenv()


# ---------------------------------------------------------
# ChromaDB configuration
# ---------------------------------------------------------

VECTOR_DB_PATH = Path("chroma_db")
COLLECTION_NAME = "tata_legal_knowledge"

_client = None
_collection = None


def _get_collection():
    """
    Lazily initialize ChromaDB.

    We intentionally do NOT load SentenceTransformer/PyTorch.
    This keeps the Render deployment lightweight enough for the
    free 512 MB instance.
    """
    global _client, _collection

    if _collection is not None:
        return _collection

    VECTOR_DB_PATH.mkdir(parents=True, exist_ok=True)

    _client = chromadb.PersistentClient(
        path=str(VECTOR_DB_PATH)
    )

    try:
        _collection = _client.get_collection(
            name=COLLECTION_NAME
        )
    except Exception:
        # Create an empty collection if the knowledge base
        # isn't present in the deployment environment.
        _collection = _client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    return _collection


# ---------------------------------------------------------
# Lightweight text retrieval
# ---------------------------------------------------------

_STOP_WORDS = {
    "the", "and", "or", "of", "to", "in", "a", "an",
    "for", "on", "by", "with", "from", "is", "are",
    "be", "this", "that", "it", "as", "at", "or",
    "may", "shall", "will", "must", "any", "each",
    "their", "its", "which", "such", "into", "than",
    "then", "there", "where", "when", "under",
}


def _tokenize(text: str) -> set:
    """
    Convert text into a small set of meaningful lowercase tokens.
    """
    if not text:
        return set()

    tokens = re.findall(r"[a-zA-Z0-9]{3,}", text.lower())

    return {
        token
        for token in tokens
        if token not in _STOP_WORDS
    }


def _score_document(query_tokens: set, document_text: str) -> float:
    """
    Calculate simple lexical similarity.

    This is intentionally lightweight and does not require
    PyTorch, transformers, or a local embedding model.
    """
    document_tokens = _tokenize(document_text)

    if not query_tokens or not document_tokens:
        return 0.0

    intersection = query_tokens.intersection(document_tokens)

    if not intersection:
        return 0.0

    # Jaccard-style overlap
    score = len(intersection) / len(query_tokens)

    # Small bonus for exact multi-word phrase matches.
    return score


# ---------------------------------------------------------
# Public retrieval function
# ---------------------------------------------------------

def retrieve_relevant_knowledge(query: str) -> List[Dict[str, Any]]:
    """
    Retrieve the most relevant organizational knowledge
    for a contract clause.

    This version intentionally avoids SentenceTransformer
    so the backend can run on a low-memory Render instance.
    """

    if not query or not query.strip():
        return []

    try:
        collection = _get_collection()

        count = collection.count()

        if count == 0:
            return []

        # Keep memory usage bounded.
        limit = min(count, 2000)

        data = collection.get(
            limit=limit,
            include=["documents", "metadatas"],
        )

        documents = data.get("documents") or []
        metadatas = data.get("metadatas") or []

        query_tokens = _tokenize(query)

        scored = []

        for index, document_text in enumerate(documents):
            if not document_text:
                continue

            score = _score_document(
                query_tokens,
                document_text
            )

            if score <= 0:
                continue

            metadata = (
                metadatas[index]
                if index < len(metadatas)
                else {}
            ) or {}

            scored.append({
                "content": document_text,
                "source": metadata.get("source"),
                "page": metadata.get("page"),
                "_score": score,
            })

        # Highest relevance first.
        scored.sort(
            key=lambda item: item["_score"],
            reverse=True
        )

        results = []

        for item in scored[:3]:
            results.append({
                "content": item.get("content", ""),
                "source": item.get("source"),
                "page": item.get("page"),
            })

        return results

    except Exception as exc:
        # Retrieval failure should not prevent Gemini from
        # analyzing the actual contract clause.
        print(
            f"Knowledge retrieval warning: {exc}"
        )

        return []
