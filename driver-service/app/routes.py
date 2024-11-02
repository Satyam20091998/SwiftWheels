from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/drivers', methods=['GET'])
def get_drivers():
    return jsonify({"message": "Driver service is running!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
