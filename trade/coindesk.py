import requests

last_price= 0
old_price=0

while True:

	price_data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
	price = float(price_data.json()["bpi"]["USD"]["rate_float"])

	if last_price != price:
		old_price = last_price


	print("Coindesk: ", price, "        ", old_price - price)
	last_price=price





# import requests

# global z
# z = 0

# while True:
#     url = "https://api.coindesk.com/v1/bpi/currentprice.json"

#     x = requests.get(url).json()
#     y = x["bpi"]["USD"]["rate_float"]
#     if z < float(y):
#         print(str(y) + "    decreased by: " + str(float(y)-z))
#         z = float(y)
#     if z > float(y):
#         print(str(y) + "          increased by: " + str(z-float(y)))
#         z = float(y)
#     else:
#         z = float(y)
#         print(y)

#     # for x in x:
#     #     print(x)