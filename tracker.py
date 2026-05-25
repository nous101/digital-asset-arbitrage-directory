import ccxt

# Connect safely to Binance Exchange (Read-Only)
exchange = ccxt.binance()

# Fetch live Ethereum price data
ticker = exchange.fetch_ticker('ETH/USDT')
live_price = ticker['last']

print(f"Live Ethereum Price: ${live_price}")
