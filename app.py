from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Loading model and encoder
model = joblib.load("logistic_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Loading symptoms in correct order
with open("symptom_list.txt", "r") as f:
    all_symptoms = [line.strip() for line in f.readlines()]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    selected_symptoms = data.get("symptoms", [])

    # Binary input vector
    input_vector = [1 if symptom in selected_symptoms else 0 for symptom in all_symptoms]

    # Getting probabilities
    raw_probs = model.predict_proba([input_vector])[0]
    prob_sum = np.sum(raw_probs)

    # If model gives junk probabilities 
    if prob_sum == 0:
        return jsonify({
            "predictions": [{
                "disease": "Unknown Condition",
                "confidence": 0.0
            }]
        })

    # Normalizing
    normalized_probs = raw_probs / prob_sum

    top_indices = np.argsort(normalized_probs)[::-1][:3]

    # Preparing response
    predictions = []
    for idx in top_indices:
        disease = str(label_encoder.inverse_transform([idx])[0])
        confidence = round(float(normalized_probs[idx]) * 100, 2)
        predictions.append({
            "disease": disease,
            "confidence": confidence
        })

    return jsonify({"predictions": predictions})

if __name__ == '__main__':
    app.run(debug=True)
