from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "API is running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        print("Incoming data:", data)

        # extract safely
        bedrooms = int(data.get("bedrooms", 0))
        bathrooms = int(data.get("bathrooms", 0))
        living_area = float(data.get("living_area", 0))
        floors = int(data.get("floors", 0))

        features = [[bedrooms, bathrooms, living_area, floors]]

        prediction = model.predict(features)

        return jsonify({
            "predicted_price": float(prediction[0])
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)