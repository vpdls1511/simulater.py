# -*- coding:utf-8 -*-
# made by chocoloate

from flask import Flask, render_template
import apiRequest

app = Flask(__name__)
values = [
    '{x:new Date(2014,08,01), y:[526.00, 529.45, 517.10, 519.85]}',
    '{x:new Date(2014,08,02), y:[518.00, 520.50, 512.00, 516.40]}',
    '{x:new Date(2014,08,03), y:[526.00, 530.50, 521.35, 522.65]}',
    '{x:new Date(2014,08,04), y:[522.65, 522.65, 509.00, 512.85]}',
    '{x:new Date(2014,08,05), y:[513.00, 516.50, 503.10, 506.35]}']

apiRequest.tickers()
apiRequest.candles("5m",":tBTCUSD/")

@app.route("/")
def main():
	return render_template('index.html'
							,btc = apiRequest.usdData[0]
							,eth = apiRequest.usdData[1]
							,eos = apiRequest.usdData[2]
                            ,value = values)

if __name__ == "__main__":
	app.run(debug='true')
