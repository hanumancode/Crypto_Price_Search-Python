import requests

while True:

	# base URLs
	globalURL = "https://api.coinmarketcap.com/v1/global/"
	tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

	# get data from CoinMarketCap GlobalURL
	r = requests.get(globalURL)
	data = r.json()

	globalMarketCap = data['total_market_cap_usd']
	bitcoin_percentage_of_market_cap = data['bitcoin_percentage_of_market_cap']

	# menu
	print()
	print("Crypto Price Query")
	print("Global cap of all cryptos: $" + str(globalMarketCap))
	print("Bitcoin dominance: " + str(bitcoin_percentage_of_market_cap) + "%")
	print("Enter 'all' or 'name of crypto' i.e. bitcoin, ripple, tron, ethereum,...")
	print()
	choice = input("Enter crypto symbol or name: ")

	if choice == "all":
		r = requests.get(tickerURL)
		data = r.json()

		for x in data:
			ticker = x['symbol']
			price = x['price_usd']

			print(ticker + ":\t\t$" + price)
		print()

	else:
		tickerURL += '/'+choice+'/'
		r = requests.get(tickerURL)
		data = r.json()

		ticker = data[0]['symbol']
		price = data[0]['price_usd']

		print(ticker + ":\t\t$" + price)
		print()

	choice2 = input("Search for another cryptocurrency price? (y/n)")
	if choice2 == "y":
		continue
	if choice2 == "n":
		break


