import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env")

class Settings:
    SQLALCHEMY_DATABASE_URL_REALESTATE = os.environ.get('SQLALCHEMY_DATABASE_URL_REALESTATE')
    SQLALCHEMY_DATABASE_URL_YA = os.environ.get("SQLALCHEMY_DATABASE_URL_YA")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
    # ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = os.environ.get("ALGORITHM")
    
    MANGA_DIR = os.environ.get("MANGA_DIR")
    MANGA_HTTP = os.environ.get("MANGA_HTTP")
    VIDEO_DIR = os.environ.get("VIDEO_DIR")
    TEMP_DIR = os.environ.get("TEMP_DIR")
    GIF_FRAMES_MIN = int(os.environ.get("GIF_FRAMES_MIN"))
    GIF_FRAMES_MAX = int(os.environ.get("GIF_FRAMES_MAX"))
    GIF_SIZE = int(os.environ.get("GIF_SIZE"))
    WASTE_DIR = os.environ.get("WASTE_DIR")
    
    DATA_GO_KR_SERVICE_KEY = os.environ.get('DATA_GO_KR_SERVICE_KEY')
settings = Settings()