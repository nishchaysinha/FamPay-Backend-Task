from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from apscheduler.schedulers.background import BackgroundScheduler
from googleapiclient.discovery import build
from bson.json_util import dumps
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")  # Load MongoDB Atlas connection string from .env file
mongo = PyMongo(app)


YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Load YouTube Data API v3 key from .env file

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=GOOGLE_API_KEY)

def fetch_youtube_videos():
    search_response = youtube.search().list(
        q="football",  # Replace with your search query
        type="video",
        part="id,snippet",
        maxResults=10
    ).execute()

    for search_result in search_response.get('items', []):
        video = {
            "_id": search_result['id']['videoId'],
            "title": search_result['snippet']['title'],
            "description": search_result['snippet']['description'],
            "published_at": datetime.datetime.strptime(search_result['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"),
            "thumbnail_url": search_result['snippet']['thumbnails']['default']['url']
        }
        mongo.db.maul.replace_one({"_id": video["_id"]}, video, upsert=True)

scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_youtube_videos, trigger="interval", seconds=10000)
scheduler.start()

@app.route('/videos', methods=['GET'])
def get_videos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    videos = mongo.db.maul.find().sort("published_at", -1).skip((page - 1) * per_page).limit(per_page)
    return dumps(videos)  # Convert BSON to JSON

if __name__ == '__main__':
    app.run(debug=True)