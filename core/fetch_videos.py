from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from utils.config import YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, GOOGLE_API_KEYS
import datetime
from __main__ import collection

def fetch_youtube_videos():
    for key in GOOGLE_API_KEYS:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=key)
        try:
            search_response = youtube.search().list(
                q="football",  # Replace with your search query
                type="video",
                part="id,snippet",
                maxResults=10
            ).execute()
        except HttpError as e:
            print(f"Failed to fetch videos from YouTube API: {e}")
            # If quota limit exceeds, switch to the next key
            if 'quotaExceeded' in str(e):
                continue
            else:
                # If it's another HttpError, continue to the next iteration
                continue

        for search_result in search_response.get('items', []):
            try:
                video = {
                    "_id": search_result['id']['videoId'],
                    "title": search_result['snippet']['title'],
                    "description": search_result['snippet']['description'],
                    "published_at": datetime.datetime.strptime(search_result['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"),
                    "thumbnail_url": search_result['snippet']['thumbnails']['default']['url']
                }
                collection.replace_one({"_id": video["_id"]}, video, upsert=True)
            except Exception as e:
                print(f"Failed to process video: {e}")