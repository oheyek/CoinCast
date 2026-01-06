"""
Tests for fetch_crypto module.
"""

import pytest
from unittest.mock import patch
from src.fetch_crypto import get_current_price, get_historical_data, cache


def test_get_current_price() -> None:
    """
    Test the get_current_price function with mocked API response.
    """
    cache.clear()
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"bitcoin": {"usd": 50000}}
        result = get_current_price("bitcoin")
        assert result == "$50000"


def test_get_historical_data() -> None:
    """
    Test the get_historical_data function with mocked API response.
    """
    cache.clear()
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"prices": [[1, 50000]]}
        result = get_historical_data("bitcoin")
        assert isinstance(result, list)
