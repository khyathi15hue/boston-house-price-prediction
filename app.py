from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import warnings
import os
warnings.filterwarnings('ignore', category=UserWarning)

app = Flask(__name__)
CORS(app)

# Load model from the same directory as this script
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)
@app.route("/")
def home():
    return "House Price Prediction API Running"


    
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

    return jsonify({"prediction": round(prediction[0],2)})

if __name__ == "__main__":
    app.run(debug=True)