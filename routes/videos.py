from __main__ import app, collection
from flask import request
from bson.json_util import dumps


@app.route('/videos', methods=['GET'])
def get_videos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    videos = collection.find().sort("published_at", -1).skip((page - 1) * per_page).limit(per_page)
    return dumps(videos)  # Convert BSON to JSON