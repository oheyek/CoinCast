from flask import Flask, render_template, request
import src.fetch_crypto

app: Flask = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        crypto_name: str = request.form.get("crypto-select-box") or ""
        current_price = src.fetch_crypto.get_current_price(crypto_name.lower())
        return render_template("index.html", current_price=current_price)
    return render_template("index.html", current_price=None)


if __name__ == "__main__":
    app.run(debug=True)
