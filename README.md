# <img src="static/img/icon-doxygen.png" alt="CoinCast Logo" width="32"/> CoinCast

![Python Version](https://img.shields.io/badge/python-3.14%2B-blue?logo=python&logoColor=white)
[![License](https://img.shields.io/github/license/oheyek/CoinCast?color=green)](LICENSE)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)
[![Docker Pulls](https://img.shields.io/docker/pulls/oheyek/coin-cast)](https://hub.docker.com/r/oheyek/coin-cast)
[![Documentation](https://img.shields.io/badge/docs-github.io-blue)](https://oheyek.github.io/CoinCast/)

A powerful web application for cryptocurrency price forecasting with an intuitive interface.

## ✨ Features

- **Multi-Crypto Support**: Fetch and analyze prices for various cryptocurrencies.
- **Real-Time Data Fetching**: Get up-to-date cryptocurrency prices instantly.
- **Price Predictions**: Predict future price trends using advanced algorithms.
- **Web-Based Interface**: Accessible from any device with a browser.
- **Linear Regression Predictions**: Predict future price trends using linear regression models.
- **Simple and Fast**: Analyze crypto data in the blink of an eye.
- **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux.
- **Containerized**: Available as a Docker image for easy deployment.
- **Comprehensive Testing**: Thoroughly tested for reliability.

## 🛠️ Installation

### Using Docker (Recommended)

1. Pull the Docker image:
   ```bash
   docker pull oheyek/coin-cast
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 oheyek/coin-cast
   ```
3. Open your browser and go to `http://localhost:5000`

### Running from Source

```bash
# Clone the repository
git clone https://github.com/oheyek/CoinCast.git
cd CoinCast

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 🎯 Usage

1. Open the application in your browser (locally only).
2. Select a cryptocurrency to analyze.
3. View real-time prices and predictions.
4. Explore forecast trends instantly.

## 📋 Supported Cryptocurrencies

| Category     | Cryptocurrencies Available          |
| ------------ | ----------------------------------- |
| **Major**    | Bitcoin (BTC), Ethereum (ETH), etc. |
| **Altcoins** | Litecoin (LTC), Ripple (XRP), etc.  |

## ⚠️ Disclaimer

This project is for educational and portfolio purposes only. It is not intended as financial or investment advice. Cryptocurrency investments are highly volatile and risky. Always do your own research and consult with a financial advisor before making investment decisions.

## 🔧 Technical Details

- **Language**: Python 3.14+
- **Web Framework**: Flask 3.1.2+
- **WSGI Server**: Gunicorn 23.0.0+
- **Testing**: pytest 9.0.2+
- **Deployment**: Docker

### Key Dependencies

```
flask>=3.1.2
gunicorn>=23.0.0
pytest>=9.0.2
```

## 🏗️ Building from Source

### Docker Build

```bash
# Build the Docker image
docker build -t coin-cast .

# Run the container
docker run -p 5000:5000 coin-cast
```

## 🗂️ Project Structure

```
CoinCast/
├── app.py                     # Flask application entry point
├── src/
│   ├── __init__.py
│   ├── fetch_crypto.py        # Crypto data fetching logic
│   ├── predict.py             # Prediction algorithms
│   └── tests/
│       ├── __init__.py
│       ├── test_fetch_crypto.py # Fetching tests
│       └── test_predict.py     # Prediction tests
├── static/
│   ├── css/
│   │   └── style.css          # Stylesheets
│   └── img/
│       ├── icon-doxygen.png
│       ├── icon.ico
│       └── icon.png           # Icons
├── templates/
│   ├── base.html              # Base template
│   └── index.html             # Home page
├── pyproject.toml             # Project configuration
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## 🧪 Testing

The project includes simple unit tests for all fetching and prediction functions.

### Running Tests

```bash
# Install test dependencies
pip install pytest

# Run all tests
pytest

# Run specific test file
pytest tests/test_fetch_crypto.py

# Run with verbose output
pytest -v
```

## 🤝 Contributions

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

**Happy Forecasting! 🎉**

## Author

Made with ❤️ by ohey<br>
[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/black_img.png)](https://www.buymeacoffee.com/ohey)

---

Due to the short limit of the free API, the site is not deployed as it can even get data once. If you find this project useful, consider buying me a coffee! ☕

