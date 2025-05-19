from fastapi import APIRouter, HTTPException
from app.schemas.category import Category
from typing import List
from app.core.database import async_db
from app.core.constants import COLLECTIONS
from pymongo.errors import PyMongoError

router = APIRouter()

@router.get("/categories", response_model=List[Category])
async def get_categories():
    try:
        cursor = async_db[COLLECTIONS["categories"]].find({})
        categories = []
        async for doc in cursor:
            categories.append(Category(**doc))
        return categories
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
