import requests

initial_capital = 8777

my_ballance_usd = 0
my_ballance_btc = 1

profit = 0

bought = initial_capital
sold = 0

last_price= 0
old_price=0

while True:
    price_data = requests.get('https://blockchain.info/ticker')
    price = float(price_data.json()["USD"]["buy"])
    # if price increased
    if last_price < price:
        old_price = last_price
        if bought < price:
            if my_ballance_usd == 0:
                my_ballance_usd = my_ballance_btc * price
                my_ballance_btc = 0
                sold = price
                bought = 100000000000
                profit = my_ballance_usd
    # if price decreased
    if last_price > price:
        old_price = last_price
        if sold > price:
            if my_ballance_btc == 0:
                my_ballance_btc = my_ballance_usd / price
                my_ballance_usd = 0
                bought = price
                sold = 0

                

    print("Blockchain: ", price, "         ", old_price - price, "       profit: ", profit-initial_capital, "          bought by:  ", bought)
    last_price=price