from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/payments', methods=['GET'])
def get_payments():
    return jsonify({"message": "Payment service is running!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
