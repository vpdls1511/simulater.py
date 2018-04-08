import json
import urllib
import threading

def coinPrice():
    time = "1m:"
    symbol = "tBTCUSD/"

    apiUrl = "https://api.bitfinex.com/v2/candles/trade:"+time+symbol+"hist"

    jsonData = urllib.urlopen(apiUrl)
    data = jsonData.read()
    dict = json.loads(data)

    print dict

def main():
    coinPrice()

if __name__ == "__main__":
    main()
