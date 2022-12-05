from tick_downloader import tick_downloader
from parse_ticks import parse_ticks
from csv_loader import csv_loader
from ibapi.contract import Contract
import pandas as pd

df_agg = pd.DataFrame()
df_list = []

with open('symbols.txt', 'r') as f:
    symbol_list = [i for i in f.read().splitlines() if i]
 
def main():
    for symbol in symbol_list:

        contract = Contract()
        contract.symbol = symbol
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        #contract.primaryExchange = "NASDAQ" 
        num_ticks = 1000  # maximum value is 1000
        date = "20221115 09:30:00 US/Eastern" #format is yyyymmdd hh:mm:ss xx/xxx where yyyymmdd and xx/xxx are optional. E.g.: 20031126 

        tick_downloader(contract, date, num_ticks)
        parse_ticks(contract.symbol)
        x = csv_loader()
        df_list.append(x)
    #print('df_list:',df_list)
    df_agg = pd.concat(df_list)
    df_agg.to_clipboard()
    df_agg.to_csv('aggregated_data.csv')
    print('df_agg: ' ,df_agg)

if __name__ == '__main__':
    main()