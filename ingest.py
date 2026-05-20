from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

docs = [
    Document(page_content="Delhi to Mumbai flight costs 5000"),
    Document(page_content="Mumbai budget hotels start at 1500")
]

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="./chroma_db"
)

db.persist()