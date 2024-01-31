from dotenv import load_dotenv
import os

load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME")  # Load MongoDB collection name from .env file
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
GOOGLE_API_KEYS = os.getenv("GOOGLE_API_KEYS").split(',')

# Path: utils/config.py