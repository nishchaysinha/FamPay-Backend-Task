from app import app
from flask import jsonify
import random

#to keep render deployment permanently active
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong!", "number": random.randint(1, 100)})