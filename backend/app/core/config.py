# App configuration
import os

class Settings:
    PROJECT_NAME: str = "Timeline API"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

settings = Settings()
