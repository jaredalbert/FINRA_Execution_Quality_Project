from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
from threading import Timer
import datetime
import time

symbols = []
with open('symbols.txt', 'r') as file:
    for symbol in file:
        symbols.append(symbol[:-1])
 

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def stop(self):
        self.done = True
        self.disconnect()



#Create contract object

stock = Contract()
stock.symbol = 'C'
stock.secType = 'STK'
stock.exchange = 'SMART'
stock.currency = "USD"

 

#queryTime = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y%m%d %H:%M:%S")

def main():
    app = TestApp()
    #app.nextValidID(8029)
    app.connect('127.0.0.1', 7497, 0)

    time.sleep(2)
    Timer(3, app.stop).start()
    #app.start()
    ret = app.reqHistoricalTicks(18005, stock, 
    "20221118 09:50:00 US/Eastern", "", 10, "MIDPOINT", 1, True, [])
    print(f"here's the return value: {ret}")
    #app.run()
 

if __name__ == '__main__':
    main()

""" 
 

#Working with Pandas DataFrames

import pandas

 

df = pandas.DataFrame(app.data, columns=['DateTime', 'Open', 'High', 'Low', 'Close', 'Volume'])

#df['DateTime'] = pandas.to_datetime(df['DateTime'],unit='s')

df.to_csv('stock.csv') 

 

print(df) """
