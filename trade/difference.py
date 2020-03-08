import requests

while True:
    url1 = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    url2 = "https://api.coindesk.com/v1/bpi/currentprice.json"

    x = requests.get(url1).json()
    y = x["data"]["amount"]
    x1 = requests.get(url2).json()
    y1 = x1["bpi"]["USD"]["rate_float"]
    print(float(y1) - float(y))