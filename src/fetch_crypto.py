import requests
from cachetools import TTLCache, cached

cache = TTLCache(maxsize=15, ttl=300)


@cached(cache)
def get_current_price(cryptocurrency):
    response = requests.get(
        f"https://api.coingecko.com/api/v3/simple/price?ids={cryptocurrency}&vs_currencies=usd"
    )
    try:
        return f"${response.json()[cryptocurrency]['usd']}"
    except KeyError:
        return "Free api time exceed, try again later."


# response = requests.get(
#     "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"
# )
