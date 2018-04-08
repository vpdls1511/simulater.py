import apiRequest
import datetime

date = apiRequest.candles("5m",":tBTCUSD/")
dateSize = len(date)
value = [1]*dateSize

for i in range(dateSize):
    value.append("{x:new Date("
     + datetime.datetime.fromtimestamp(int(date[i][0])/1000).strftime("%Y,%m,%d %H:%M:%S") +
     "), y:["
     + str(date[i][1]) #open
     + str(date[i][3]) #hight
     + str(date[i][4]) #low
     + str(date[i][2]) + #close
     "]}")

print value


#{x:new Date(2014,08,01), y:[526.00, 529.45, 517.10, 519.85]}
