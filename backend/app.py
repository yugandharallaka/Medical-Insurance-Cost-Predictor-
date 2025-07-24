from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # ✅ This enables CORS for all routes

# Load models and scalers
rf = pickle.load(open('models/random_forest.pkl', 'rb'))
input_scaler = pickle.load(open('models/input_scaler.pkl', 'rb'))
output_scaler = pickle.load(open('models/output_scaler.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[
        data['age'], data['sex'], data['bmi'], data['children'],
        data['smoker'], data['region'],
        data['age'] * data['bmi'],
        data['bmi'] ** 2,
        data['age'] * data['smoker'],
        data['bmi'] * data['smoker'],
        data['age'] * data['bmi'] * data['smoker']
    ]])

    features_scaled = features.astype(float)
    features_scaled[:, [0, 2, 6, 7, 8, 9, 10]] = input_scaler.transform(features_scaled[:, [0, 2, 6, 7, 8, 9, 10]])

    prediction_scaled = rf.predict(features_scaled)
    prediction_actual = output_scaler.inverse_transform(prediction_scaled.reshape(-1, 1))

    return jsonify({'predicted_cost': float(prediction_actual[0][0])})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
