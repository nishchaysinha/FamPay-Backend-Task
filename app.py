from flask import Flask

app = Flask(__name__) #create the Flask app

from utils.db import get_db

collection = get_db()

import utils.scheduler as scheduler
import routes.videos
import routes.ping


scheduler.start_scheduler()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
