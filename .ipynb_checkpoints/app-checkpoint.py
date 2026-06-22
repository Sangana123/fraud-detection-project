from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Charger modèle
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():

    features = np.array([[

        float(request.form['transactions_last_24h']),
        float(request.form['transactions_last_1h']),
        float(request.form['amount_aed']),
        float(request.form['items_count']),
        float(request.form['hour']),
        float(request.form['day_of_week']),
        float(request.form['avg_item_price']),

        int(request.form['payment_method_bank_transfer']),
        int(request.form['payment_method_card']),
        int(request.form['payment_method_google_pay']),
        int(request.form['payment_method_paypal']),

        float(request.form['ip_risk_score'])

    ]])

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        result = "⚠️ Transaction frauduleuse"
    else:
        result = "✅ Transaction légitime"

    return render_template(
        'index.html',
        prediction_text=result,
        probability=round(probability * 100, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)