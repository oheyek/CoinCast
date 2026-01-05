import requests


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
# print(response.json())
#
# response = requests.get("https://api.coingecko.com/api/v3/coins/list")
# print(response.json())
#
# get_current_price("bitcoin")
# get_current_price("ethereum")
# get_current_price("tether")
# get_current_price("binancecoin")
# get_current_price("solana")
# get_current_price("ripple")
# get_current_price("cardano")
# get_current_price("dogecoin")
get_current_price("polkadot")
