"""
CoinCast Flask application.

This module contains the main Flask app for CoinCast, handling routes for crypto price fetching and prediction.
"""

from flask import Flask, render_template, request
import src.fetch_crypto
import src.predict

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main() -> str:
    """
    Main route handler for GET and POST requests.

    Handles crypto price fetching and prediction based on form data.

    @return: Rendered HTML template as string.
    """
    crypto_name = None
    current_price = None
    forecast_data = None

    if request.method == "POST":
        crypto_name = request.form.get("crypto-select-box") or ""
        action = request.form.get("action")

        if action == "get_price":
            current_price = src.fetch_crypto.get_current_price(crypto_name.lower())
        elif action == "get_forecast":
            current_price = src.fetch_crypto.get_current_price(crypto_name.lower())
            forecast_data = src.predict.predict_crypto_data(crypto_name.lower())

    return render_template(
        "index.html",
        crypto_name=crypto_name,
        current_price=current_price,
        forecast_data=forecast_data,
    )


if __name__ == "__main__":
    app.run(debug=False)
