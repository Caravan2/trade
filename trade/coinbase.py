import requests

last_price= 0
old_price=0

while True:

	price_data = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
	price = float(price_data.json()["data"]["amount"])

	if last_price != price:
		old_price = last_price


	print("Coinbase: ", price, "         ", old_price - price)
	last_price=price






# import requests

# global z
# z = 0

# while True:
#     url = "https://api.coinbase.com/v2/prices/spot?currency=USD"

#     x = requests.get(url).json()
#     y = x["data"]["amount"]
#     if z < float(y):
#         print(str(y) + "    decreased by: " + str(float(y)-z))
#         z = float(y)
#     if z > float(y):
#         print(str(y) + "          increased by: " + str(z-float(y)))
#         z = float(y)
#     else:
#         z = float(y)
#         print(y)