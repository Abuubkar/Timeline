from fastapi import FastAPI
from app.api.v1.endpoints import category

app = FastAPI()

app.include_router(category.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Timeline FastAPI backend!"}
