from pathlib import Path
from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings
model=SentenceTransformer('all-MiniLM-L6-v2')
class SentenceTransformerEmbeddings(Embeddings):
    def embed_documents(self,texts): return model.encode(texts,batch_size=32,show_progress_bar=False).tolist()
    def embed_query(self,text): return model.encode([text],show_progress_bar=False)[0].tolist()
embedding_function=SentenceTransformerEmbeddings()
VECTOR_DB_PATH=Path(__file__).resolve().parents[1]/'chroma_db'
vector_store=Chroma(collection_name='tata_legal_knowledge',embedding_function=embedding_function,persist_directory=str(VECTOR_DB_PATH))
retriever=vector_store.as_retriever(search_kwargs={'k':3})
def retrieve_relevant_knowledge(query):
    if not query or not query.strip(): return []
    return [{'content':d.page_content,'source':d.metadata.get('source'),'page':d.metadata.get('page')} for d in retriever.invoke(query)]
def retrieve_relevant_knowledge_batch(queries,k=3):
    clean=[q.strip() if q else '' for q in queries]
    if not clean:return []
    embs=model.encode(clean,batch_size=32,show_progress_bar=False).tolist()
    result=vector_store._collection.query(query_embeddings=embs,n_results=k,include=['documents','metadatas'])
    out=[]
    for docs,metas in zip(result.get('documents',[]),result.get('metadatas',[])):
        out.append([{'content':c,'source':(m or {}).get('source'),'page':(m or {}).get('page')} for c,m in zip(docs or [],metas or [])])
    return out
