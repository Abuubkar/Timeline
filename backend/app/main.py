from fastapi import FastAPI
from app.api.v1.endpoints import example

app = FastAPI()

app.include_router(example.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Timeline FastAPI backend!"}
