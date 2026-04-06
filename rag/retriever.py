from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

load_dotenv()

def load_vector_store():
    loader = TextLoader("data/sample_docs/docs.txt")
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    return db

def retrieve_docs(query: str):
    db = load_vector_store()
    results = db.similarity_search(query, k=2)

    context = " ".join([doc.page_content for doc in results])
    return context