# -*- coding:utf-8 -*-
# made by chocoloate

from flask import Flask, render_template
import threading
import json
import urllib
import datetime

app = Flask(__name__)
lPrice = "last_price"

symbols = "tBTCUSD,tETHUSD,tEOSUSD"
symbolCount = symbols.count("t")
usdData = [1]*symbolCount

def coinPrice():
    apiUrl = "https://api.bitfinex.com/v2/tickers?symbols="+symbols
    jsonData = urllib.urlopen(apiUrl)
    data = jsonData.read()
    dict = json.loads(data)

    for i in range(symbolCount):
		usdData[i] = dict[i][7]
		print usdData[i]

    threading.Timer(5,coinPrice).start()
coinPrice()

@app.route("/")
def main():
	return render_template('index.html'
							,btc = usdData[0]
							,eth = usdData[1]
							,eos = usdData[2])

if __name__ == "__main__":
	app.run(debug='true')
