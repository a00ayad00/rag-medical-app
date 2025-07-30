from fastapi import FastAPI
import uvicorn
from src.rag import invoke_query

app = FastAPI(
    title="Welcome to the RAG Medical App",
    description="This is a RAG Medical App that uses LangChain to answer medical queries."
)


@app.post("/query")
async def query(query: str):
    """
    Endpoint to query the RAG system.
    
    Args:
        query (str): The medical query to be answered.
    
    Returns:
        dict: The response from the RAG system.
    """
    response = invoke_query(query)
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)