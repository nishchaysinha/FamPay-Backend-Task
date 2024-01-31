from __main__ import app

from flask_pymongo import PyMongo
from utils.config import COLLECTION_NAME
import os

def get_db():
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")  # Load MongoDB Atlas connection string from .env file
    mongo = PyMongo(app)
    collection = getattr(mongo.db, COLLECTION_NAME)
    return collection