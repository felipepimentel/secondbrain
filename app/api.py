from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from secondbrain.search_engine import SearchEngine
from secondbrain.weaviate_client import WeaviateClient

app = FastAPI()

weaviate_client = WeaviateClient("http://weaviate:8080")
search_engine = SearchEngine(weaviate_client)

class SearchQuery(BaseModel):
    query: str

@app.post("/search")
async def search(search_query: SearchQuery):
    results = search_engine.search(search_query.query)
    return {"results": results}

@app.post("/index")
async def index_document(document: dict):
    try:
        weaviate_client.index_document(document)
        return {"message": "Document indexed successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/document")
async def delete_document(file_path: str):
    try:
        weaviate_client.delete_document(file_path)
        return {"message": "Document deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}