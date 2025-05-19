import os
from pymongo import MongoClient, AsyncMongoClient

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGODB_DB", "timeline")

# For sync usage (not recommended for FastAPI async endpoints)
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

# For async usage (recommended)
async_client = AsyncMongoClient(MONGODB_URI)
async_db = async_client[DB_NAME]

# Usage:
# from app.core.database import async_db
# await async_db["collection_name"].find_one({})
