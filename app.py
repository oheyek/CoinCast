from flask import Flask

app: Flask = Flask(__name__)


@app.route("/")
def main():
    return "<p> Flask Server </p>"


if __name__ == "__main__":
    app.run(debug=True)
