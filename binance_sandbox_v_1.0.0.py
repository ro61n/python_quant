import requests

#Binance Rest API GitHub:
#https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md
#the github page is basically a user manual detailing how to use their api
#the response format is also shown on github for each type of request below


### General Queries (for all currency pairs) below:

#A - "Symbol price ticker"
#** You can specify a symbol (as shown in #D). if you don't then the prices for all currency pairs will be returned
a = requests.get("https://api.binance.com/api/v3/ticker/price").json()
print ("A [begin]")
print (a)
print ("A [end]")

#B - "24hr ticker price change statistics" - basically the same as A but with more information returned
#** You can specify a symbol (as shown in #D). If you don't then the info for all currency pairs will be returned
b = requests.get("https://api.binance.com/api/v3/ticker/24hr").json()
print ("B [begin]")
print (b)
print ("B [end]")

#C - "Symbol order book ticker" - basically the same as A but returning the order book bid/ask prices and quantities.
#** You can specify a symbol (as shown in #D). If you don't then the info for all currency pairs will be returned
c = requests.get("https://api.binance.com/api/v3/ticker/bookTicker").json()
print ("C [begin]")
print (c)
print ("C [end]")

### Queries related to a specific currency pair below:

#D - "Order book": basically the spread
symbol = "BTCUSDT" #you can change the symbol to any currency pair (listed in A above)
limit = "5" # i.e. show the 5 highest bids and 5 lowest asks. Can also be: [5, 10, 20, 50, 100, 500, 1000, 5000]
d = requests.get("https://api.binance.com/api/v3/depth?symbol="+symbol+'&limit='+limit).json()
print ("D [begin]")
print (d)
print ("D [end]")

#E - "Kline/Candlestick data"
symbol = "BTCUSDT"
interval = "30m" #30 minute chart interval. Can be [1m 3m 5m 15m 30m 1h 2h 4h 6h 8h 12h 1d 3d 1w 1M]
startTime = "" #not required - "Unix epoch" time format - there should be a python module that can convert human readable time into and out of this format - I will have a look.
endTime = "" #not required
limit = "100" # show data for the most recent 100 '30 minute' bars. You can either use "limit" or "start and end time".
e = requests.get("https://api.binance.com/api/v3/klines?symbol="+symbol+"&interval="+interval+"&limit="+limit).json()
print ("E [begin]")
print (e)
print ("E [end]")
