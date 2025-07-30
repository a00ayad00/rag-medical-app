from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_core.documents.base import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def pdf_loader(pdf_path):
    """Load a PDF file and split it into chunks."""
    loader = DirectoryLoader(pdf_path, glob="*.pdf", loader_cls=PyPDFLoader)

    return loader.load()


def meta_filter(docs: list[Document]) -> list[Document]:
    """Filter documents based on metadata."""
    final_docs = []
    for doc in docs:
        source = doc.metadata['source']
        page = doc.metadata['page']
        final_docs.append(Document(
            page_content=doc.page_content,
            metadata={
                'source': source,
                'page': page
            }
        ))

    return final_docs


def text_splitter(docs: list[Document]) -> list[Document]:
    """Split documents into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=80)
    
    return text_splitter.split_documents(docs)