from apscheduler.schedulers.background import BackgroundScheduler
from utils.config import TIME_DELTA
from core.fetch_videos import fetch_youtube_videos

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=fetch_youtube_videos, trigger="interval", seconds=TIME_DELTA)
    scheduler.start()