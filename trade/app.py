from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
import requests, threading

    

app = Flask(__name__)
CORS(app)
socket_io = SocketIO(app)




def background_stuff():
	coinbase_last_price=0
	coindesk_last_price=0
	coinbase_old_price=0
	coindesk_old_price=0
	while True:
		coinbase_data = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
		coindesk_data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')


		
		coinbase_price = float(coinbase_data.json()["data"]["amount"])
		coindesk_price = coindesk_data.json()["bpi"]["USD"]["rate_float"]

		if coindesk_last_price != coindesk_price:
			coindesk_old_price = coindesk_last_price

		if coinbase_last_price != coinbase_price:
			coinbase_old_price = coinbase_last_price

		socket_io.emit("price", {
			"coindesk":{
				"api": "coindesk",
				"changing": coindesk_old_price - coindesk_price,
				"price": coindesk_price,
			},
			"coinbase":{
				"api": "coinbase",
				"changing": coinbase_old_price - coinbase_price,
				"price": coinbase_price,
			}
		})
		coindesk_last_price=coindesk_price
		coinbase_last_price=coinbase_last_price

@app.route('/')
def draw():
	return render_template('main.html')



if __name__ == '__main__':
	checking = threading.Thread(target=background_stuff)
	checking.start()
	socket_io.run(app, debug=True, host='localhost', port=5000)
	
