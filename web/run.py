# -*- coding:utf-8 -*-
# made by chocoloate

from flask import Flask, render_template
import apiRequest

app = Flask(__name__)

apiRequest.tickers()
apiRequest.candles("5m",":tBTCUSD/")

@app.route("/")
def main():
	return render_template('index.html'
							,btc = apiRequest.usdData[0]
							,eth = apiRequest.usdData[1]
							,eos = apiRequest.usdData[2])

if __name__ == "__main__":
	app.run(debug='true')
