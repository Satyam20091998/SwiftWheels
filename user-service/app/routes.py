from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for the app

@app.route('/drivers', methods=['GET'])
def get_drivers():
    return jsonify({"message": "Driver service is running!"}), 200

@app.route('/register', methods=['POST'])
def register_user():
    # Registration logic goes here
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
