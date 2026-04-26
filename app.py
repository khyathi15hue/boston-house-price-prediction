from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import warnings
import os

warnings.filterwarnings('ignore', category=UserWarning)

# Serve React build
app = Flask(__name__, static_folder="frontend/build", static_url_path="")
CORS(app)

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Serve React UI
@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = [
        float(data["CRIM"]),
        float(data["ZN"]),
        float(data["INDUS"]),
        float(data["CHAS"]),
        float(data["NOX"]),
        float(data["RM"]),
        float(data["AGE"]),
        float(data["DIS"]),
        float(data["RAD"]),
        float(data["TAX"]),
        float(data["PTRATIO"]),
        float(data["B"]),
        float(data["LSTAT"])
    ]

    prediction = model.predict([features])

    return jsonify({"prediction": round(prediction[0], 2)})

# React route handling
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(debug=True)