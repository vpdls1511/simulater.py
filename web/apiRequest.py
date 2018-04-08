import json, urllib, threading, datetime

symbols = "tBTCUSD,tETHUSD,tEOSUSD"
symbolCount = symbols.count("t")
usdData = [1]*symbolCount
value=[1]*120

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

def chart(date,dateSize):

    print ("Update chart data")
    for i in range(dateSize):
        time = datetime.datetime.fromtimestamp(int(date[i][0])/1000).strftime('%Y,%m,%d,%H,%M,%S')
        value[i] ="{x:new Date(" + time + "), y:[" + str(date[i][1]) + "," + str(date[i][3]) + "," + str(date[i][4]) + "," + str(date[i][2]) + "]}"
    # --- open , hight, low, close --->>
    threading.Timer(7,chart,[date,dateSize]).start()
