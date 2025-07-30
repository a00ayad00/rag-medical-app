from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from src.utils import pdf_loader, meta_filter, text_splitter
from src.models import embedding_model


load_dotenv()


pc = Pinecone()
index_name = "medical-rag"


if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1',
        ),
        dimension=384,
        metric="cosine"
    )

    docs = pdf_loader("pdfs")
    docs = meta_filter(docs)
    splits = text_splitter(docs)

    vector_store = PineconeVectorStore.from_documents(
        documents = splits,
        embedding = embedding_model,
        index_name = index_name
    )
else:
    vector_store = PineconeVectorStore.from_existing_index(
        embedding=embedding_model,
        index_name=index_name
    )


retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3},
)