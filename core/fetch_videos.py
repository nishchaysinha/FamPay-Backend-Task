from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from utils.config import YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, GOOGLE_API_KEYS, QUERY, TIME_DELTA
import datetime
from app import collection


def fetch_youtube_videos():
    for key in GOOGLE_API_KEYS:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=key)
        try:
            search_response = youtube.search().list(
                q=QUERY,
                type="video",
                part="id,snippet",
                maxResults=100,
                publishedAfter=(datetime.datetime.utcnow() - datetime.timedelta(seconds=TIME_DELTA)).isoformat('T') + 'Z', 
                #Having an issue where providing a timedelta gives me 0 acceptable results i will try increasing the time delta in hopes for it to work 
            ).execute()

            for search_result in search_response.get('items', []):
                video_data = {
                    '_id': search_result['id']['videoId'],
                    'title': search_result['snippet']['title'],
                    'description': search_result['snippet']['description'],
                    'publishedAt': search_result['snippet']['publishedAt'],
                    'thumbnails': search_result['snippet']['thumbnails'],
                    # Add any other fields you need
                }
                collection.replace_one({'_id': video_data['_id']}, video_data, upsert=True)

            print(f"Successful fetch from YouTube API: {key}")
        except HttpError as e:
            print(f"Failed to fetch videos from YouTube API: {key}, Using next available key")
            if 'quotaExceeded' in str(e):
                continue
            else:
                print(f"Error details: {str(e)}")
                continue