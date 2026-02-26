from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # API Keys (all free tier)
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./neoclawd.db")
    
    # API Settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    
    # Cache
    CACHE_TTL: int = 3600  # 1 hour
    
    # Model preferences (lightest to heaviest)
    MODEL_PRIORITY: list = ["ollama", "deepseek", "openrouter"]
    
    class Config:
        env_file = ".env"

settings = Settings()