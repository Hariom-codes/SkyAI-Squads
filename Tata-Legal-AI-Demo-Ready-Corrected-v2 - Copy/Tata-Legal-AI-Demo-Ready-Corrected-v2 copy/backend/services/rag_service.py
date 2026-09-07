import os
from pathlib import Path

from google import genai
from google.genai import types

from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

VECTOR_DB_PATH = Path("chroma_db")
COLLECTION_NAME = "tata_legal_knowledge"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not configured")

client = genai.Client(api_key=GOOGLE_API_KEY)


# ---------------------------------------------------------
# Gemini Embeddings
# ---------------------------------------------------------

class GeminiEmbeddings(Embeddings):

    MODEL_NAME = "gemini-embedding-001"
    DIMENSION = 768

    def embed_documents(self, texts):
        if not texts:
            return []

        response = client.models.embed_content(
            model=self.MODEL_NAME,
            contents=texts,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_DOCUMENT",
                output_dimensionality=self.DIMENSION,
            ),
        )

        return [embedding.values for embedding in response.embeddings]

    def embed_query(self, text):
        if not text or not text.strip():
            return []

        response = client.models.embed_content(
            model=self.MODEL_NAME,
            contents=text,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_QUERY",
                output_dimensionality=self.DIMENSION,
            ),
        )

        return response.embeddings[0].values


# ---------------------------------------------------------
# Embedding + Vector Store
# ---------------------------------------------------------

embedding_function = GeminiEmbeddings()

vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=embedding_function,
    persist_directory=str(VECTOR_DB_PATH),
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)


# ---------------------------------------------------------
# Retrieval
# ---------------------------------------------------------

def retrieve_relevant_knowledge(query: str) -> list:

    if not query or not query.strip():
        return []

    try:
        documents = retriever.invoke(query)

        results = []

        for document in documents:
            results.append(
                {
                    "content": document.page_content,
                    "source": document.metadata.get("source"),
                    "page": document.metadata.get("page"),
                }
            )

        return results

    except Exception as exc:
        print(f"RAG retrieval error: {exc}")
        return []