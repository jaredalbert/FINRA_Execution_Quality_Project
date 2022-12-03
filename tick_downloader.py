from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.ticktype import TickTypeEnum
from threading import Timer
import time
import pandas as pd
import pickle
from parse_ticks import parse_ticks


class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
    
    def stop(self):
        self.done = True
        self.disconnect()


    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def tickPrice(self, reqId, tickType, price, attrib):
        print("Tick Price. Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Price:", price, end=' ')

    def tickSize(self, reqId, tickType, size):
        print("Tick Size. Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)

""" contract = Contract()
contract.symbol = "ibm"
contract.secType = "STK"
contract.exchange = "SMART"
contract.currency = "USD"
contract.primaryExchange = "NASDAQ"   """ 
   
            
        
def tick_downloader(contract, num_ticks):
    app = TestApp()

    app.connect("127.0.0.1", 7497, 0)
    time.sleep(2)
    Timer(3, app.stop).start()
    """ contract = Contract()
    contract.symbol = "refr"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ" """
    
    
    app.reqHistoricalTicks(18028, contract,
    "20221111 09:39:33 US/Eastern", "", num_ticks, "BID_ASK", 1, True, [])
    app.reqHistoricalTicks(18029, contract,
    "20221111 09:39:33 US/Eastern", "", num_ticks, "TRADES", 1, True, [])
    #print(f'x:{x}')
    app.run()

#time.sleep(15)
#parse_ticks()
#df_bid_ask = pd.read_csv('df_bid_ask.csv')
#df_bid_ask['Symbol'] = contract.symbol
#print('df: ', df_bid_ask[' PriceAsk'])

    
""" 
time.sleep(5)
with open ('bid_ask.pk', 'rb') as f:
    vars = pickle.load(f) 

vars_list = list(vars)
l = []
d={}
for item in vars_list:
    x = str(item).split(',')
    for field in x:
        y = list(str(field).split(':'))
        if y[0] not in d.keys():
            d[y[0]] = (y[1])
        else:
            d[y[0]]+=((y[1]))
    

            
new_d = {k:v.split(' ') for k, v in d.items()}        
df = pd.DataFrame.from_dict(new_d, orient = 'columns')
df['Symbol'] = contract.symbol
print (df) """
    #app.tickByTickAllLast()
   
    #app.reqHistoricalTicks(18025, contract,
    #"20221111 09:39:33 US/Eastern", "", 10, "TRADES", 1, True, [])
    #app.historicalTicks(18005, 10, True)
    #app.historicalTicksBidAsk(18005, 10, True)

    #print(f'done {ticks}')

    #app.run()


if __name__ == "__main__":
    tick_downloader(contract, 10)