import pytest
from unittest.mock import patch
from src.predict import predict_crypto_data


def test_predict_crypto_data():
    prices = [50000 + i * 100 for i in range(30)]
    with patch("src.predict.get_historical_data") as mock_get:
        mock_get.return_value = prices
        result = predict_crypto_data("bitcoin")
        assert isinstance(result, dict)
