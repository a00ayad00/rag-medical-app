from langchain.embeddings import HuggingFaceEmbeddings
import torch
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

embedding_model = HuggingFaceEmbeddings(
    model_name = 'sentence-transformers/all-MiniLM-L6-v2',
    model_kwargs = {
        "device": "cuda" if torch.cuda.is_available() else "cpu"
    }
)


llm = ChatGroq(model="llama3-8b-8192")