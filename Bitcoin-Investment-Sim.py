import requests
from datetime import datetime
from time import time,sleep
from matplotlib import pyplot as plt


time1 = datetime.now().strftime("%H:%M:%S")
bitPriceList = list()
timeList= list()

i=0

while i<100:
    i=i+1
    print(i)
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    time = datetime.now().strftime("%H:%M:%S")

    response = requests.get(url).json()
    usd = response["USD"]


    sleep(20 % 60)
    bitPriceList.append(usd)
    timeList.append(time)

plt.xlabel("TIME")
plt.ylabel("BITCOIN-PRICE")
plt.xticks(rotation=90)
plt.plot(timeList,bitPriceList)
plt.show()


