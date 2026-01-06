"""
Crypto fetching module.

This module provides functions to fetch current and historical crypto prices from CoinGecko API.
"""

import requests
from cachetools import TTLCache, cached
from typing import List, Union

cache = TTLCache(maxsize=15, ttl=300)


@cached(cache)
def get_current_price(cryptocurrency: str) -> str:
    """
    Get the current price of a cryptocurrency in USD.

    @param cryptocurrency: The name of the cryptocurrency (e.g., 'bitcoin').

    @return: The current price formatted as a string (e.g., '$50000'), or an error message.
    """
    response = requests.get(
        f"https://api.coingecko.com/api/v3/simple/price?ids={cryptocurrency}&vs_currencies=usd"
    )
    try:
        return f"${response.json()[cryptocurrency]['usd']}"
    except KeyError:
        return "Free api time exceed, try again later."


@cached(cache)
def get_historical_data(cryptocurrency: str) -> Union[List[float], str]:
    """
    Get historical price data for a cryptocurrency over the last 30 days.

    @param cryptocurrency: The name of the cryptocurrency (e.g., 'bitcoin').

    @return: List of prices or an error message string.
    """
    try:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/coins/{cryptocurrency}/market_chart?vs_currency=usd&days=30"
        )
        data = response.json()
        return [item[1] for item in data["prices"]]
    except KeyError:
        return "Free api time exceed, try again later."
