import requests

response = requests.get(
    "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
)
print(response.json())

response = requests.get(
    "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"
)
print(response.json())

response = requests.get("https://api.coingecko.com/api/v3/coins/list")
print(response.json())
