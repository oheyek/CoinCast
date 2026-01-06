"""
Tests for predict module.
"""

import pytest
from unittest.mock import patch
from src.predict import predict_crypto_data
from src.fetch_crypto import cache


def test_predict_crypto_data() -> None:
    """
    Test the predict_crypto_data function with mocked historical data.
    """
    cache.clear()
    prices = [50000 + i * 100 for i in range(30)]
    with patch("src.fetch_crypto.get_historical_data") as mock_get:
        mock_get.return_value = prices
        result = predict_crypto_data("bitcoin")
        assert isinstance(result, dict)
