from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/rides', methods=['GET'])
def get_rides():
    return jsonify({"message": "Ride service is running!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
