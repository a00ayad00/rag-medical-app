from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from src.vector_store import retriever
from src.models import llm
from src.prompts import system_prompt


prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])


qa_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, qa_chain)


def invoke_query(query: str):
    """Invoke the retrieval chain with a query."""
    return retrieval_chain.invoke({"input": query})