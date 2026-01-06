import numpy as np
from sklearn.linear_model import LinearRegression
from fetch_crypto import get_historical_data
from cachetools import TTLCache, cached

cache = TTLCache(maxsize=15, ttl=300)


@cached(cache)
def predict_crypto_data(cryptocurrency):
    prices = get_historical_data(cryptocurrency)
    if isinstance(prices, str):
        raise RuntimeError(prices)

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
