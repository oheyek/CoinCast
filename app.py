from flask import Flask, render_template, request
import src.fetch_crypto
import src.predict

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
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
    app.run(debug=True)
