from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from model import predict_sentiment

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']
    sentiment = predict_sentiment(text)  # Call model
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run()

