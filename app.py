from flask import Flask, render_template, request
import numpy as np
import joblib

# Initialisation de l'application Flask
app = Flask(__name__)

# Chargement des modèles
model_baseline = joblib.load("model_baseline.pkl")
model_enriched = joblib.load("model_enriched.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Modèle choisi par l'utilisateur
    model_type = request.form['model_type']

    # Variables communes aux deux modèles
    transactions_last_24h = float(request.form['transactions_last_24h'])
    transactions_last_1h = float(request.form['transactions_last_1h'])
    amount_aed = float(request.form['amount_aed'])
    items_count = float(request.form['items_count'])
    hour = float(request.form['hour'])
    day_of_week = float(request.form['day_of_week'])
    avg_item_price = float(request.form['avg_item_price'])
    payment_method_bank_transfer = int(request.form['payment_method_bank_transfer'])
    payment_method_card = int(request.form['payment_method_card'])
    payment_method_google_pay = int(request.form['payment_method_google_pay'])
    payment_method_paypal = int(request.form['payment_method_paypal'])

    # Score IP (utilisé uniquement par le modèle enrichi)
    ip_risk_score = request.form.get('ip_risk_score', '')
    if ip_risk_score == '':
        ip_risk_score = 0
    else:
        ip_risk_score = float(ip_risk_score)

    # Variables du modèle enrichi (12 variables)
    features_enriched = np.array([[
        transactions_last_24h,
        transactions_last_1h,
        amount_aed,
        items_count,
        hour,
        day_of_week,
        avg_item_price,
        payment_method_bank_transfer,
        payment_method_card,
        payment_method_google_pay,
        payment_method_paypal,
        ip_risk_score
    ]])

    # Variables du modèle standard (11 variables)
    features_baseline = np.array([[
        transactions_last_24h,
        transactions_last_1h,
        amount_aed,
        items_count,
        hour,
        day_of_week,
        avg_item_price,
        payment_method_bank_transfer,
        payment_method_card,
        payment_method_google_pay,
        payment_method_paypal
    ]])

    # Sélection du modèle
    if model_type == "baseline":
        prediction = model_baseline.predict(features_baseline)[0]
        probability = model_baseline.predict_proba(features_baseline)[0][1]
        model_used = "Random Forest standard"
    else:
        prediction = model_enriched.predict(features_enriched)[0]
        probability = model_enriched.predict_proba(features_enriched)[0][1]
        model_used = "Random Forest enrichi par réputation IP"

    # Interprétation du résultat
    if prediction == 1:
        result = "⚠️ Transaction frauduleuse"
    else:
        result = "✅ Transaction légitime"

    return render_template(
        'index.html',
        prediction_text=result,
        probability=round(probability * 100, 2),
        model_used=model_used
    )

if __name__ == '__main__':
    app.run(debug=True)