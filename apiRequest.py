import json, urllib, threading

symbols = "tBTCUSD,tETHUSD,tEOSUSD"
symbolCount = symbols.count("t")
usdData = [1]*symbolCount

def tickers():
    threading.Timer(7,tickers).start()

    apiUrl = "https://api.bitfinex.com/v2/tickers?symbols="+symbols
    jsonData = urllib.urlopen(apiUrl)
    data = jsonData.read()
    dict = json.loads(data)

    for i in range(symbolCount):
		usdData[i] = dict[i][7]
		print usdData[i]

    return usdData

def candles(time,symbol):

    apiUrl = "https://api.bitfinex.com/v2/candles/trade:"+time+symbol+"hist"

    jsonData = urllib.urlopen(apiUrl)
    data = jsonData.read()
    dict = json.loads(data)

    return dict
