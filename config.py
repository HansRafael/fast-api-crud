
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings():
    MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_USER: str = os.getenv("MYSQL_USER")

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    APP_PORT: int = os.getenv("APP_PORT")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    class Config:
        env_file = ".env"

settings = Settings()