# App configuration
import os

class Settings:
    PROJECT_NAME: str = "Timeline API"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

settings = Settings()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "timeline")
