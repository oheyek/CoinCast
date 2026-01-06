"""
Crypto prediction module.

This module provides functions to predict future crypto prices using linear regression.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from src.fetch_crypto import get_historical_data
from cachetools import TTLCache, cached
from typing import Dict, Union

cache = TTLCache(maxsize=15, ttl=300)


@cached(cache)
def predict_crypto_data(cryptocurrency: str) -> Union[Dict[int, str], str]:
    """
    Predict future crypto prices using linear regression on historical data.

    @param cryptocurrency: The name of the cryptocurrency.

    @return: Dictionary of predicted prices for future days or an error message.
    """
    prices = get_historical_data(cryptocurrency)
    if isinstance(prices, str):
        return prices

    prices = np.array(prices[-30:])

    days = np.arange(1, 31).reshape(-1, 1)
    y = prices

    model = LinearRegression()
    model.fit(days, y)

    future_days = np.arange(31, 61).reshape(-1, 1)
    future_predictions = model.predict(future_days)

    return {
        int(day): f"{price:.2f} USD"
        for day, price in zip(future_days.flatten(), future_predictions)
    }
