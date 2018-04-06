import json
import urllib
import threading

def coinPrice():

    symbols = "tBTCUSD,tETHUSD,tEOSUSD,tLTCUSD,tXRPUSD"
    symbolCount = symbols.count("t")
    apiUrl = "https://api.bitfinex.com/v2/tickers?symbols="+symbols

    jsonData = urllib.urlopen(apiUrl)
    data = jsonData.read()
    dict = json.loads(data)

    for i in range(symbolCount):
        print dict[i][0] + ":" + str(dict[i][7])
    print("")

    threading.Timer(5,coinPrice).start()

def main():
    coinPrice()

if __name__ == "__main__":
    main()
