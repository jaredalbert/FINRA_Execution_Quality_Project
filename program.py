from tick_downloader import tick_downloader
from parse_ticks import parse_ticks
from csv_loader import csv_loader
from ibapi.contract import Contract
import pandas as pd

df_agg = pd.DataFrame()
df_list = []
symbol_list =['refr', 'zionl', 'c prn']

def main():
    for symbol in symbol_list:

        contract = Contract()
        contract.symbol = symbol
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        #contract.primaryExchange = "NASDAQ" 
        num_ticks = 100 

        tick_downloader(contract, num_ticks)
        parse_ticks(contract.symbol)
        x = csv_loader()
        df_list.append(x)
    #print('df_list:',df_list)
    df_agg = pd.concat(df_list)
    df_agg.to_clipboard()
    print('df_agg: ' ,df_agg)

if __name__ == '__main__':
    main()