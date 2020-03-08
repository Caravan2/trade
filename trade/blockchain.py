import requests

last_price= 0
old_price=0

while True:

	price_data = requests.get('https://blockchain.info/ticker')
	price = float(price_data.json()["USD"]["buy"])

	if last_price != price:
		old_price = last_price


	print("Blockchain: ", price, "         ", old_price - price)
	last_price=price
