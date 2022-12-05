import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
df_agg = pd.DataFrame()
def csv_loader():
    df_bid_ask = pd.read_csv('df_bid_ask.csv', header=0,  skiprows=[1], dtype={'Time': np.int64, ' SizeBid': int, ' SizeAsk': int})
    df_bid_ask.dropna(axis=0, inplace=True)
    df_bid_ask['Time_copy_Bid_Ask']=(df_bid_ask['Time'])
    df_bid_ask['Time_copy_Bid_Ask']= df_bid_ask['Time_copy_Bid_Ask'].astype(str)
    #print('bid_ask', df_bid_ask, df_bid_ask.info())

    df_trades = pd.read_csv('df_trades.csv', header=0,  skiprows=[1], dtype = {'Time': np.int64})
    df_trades.dropna(axis=0, inplace = True)
    df_trades.set_index('Time', inplace=True)


    #print('trades:', df_trades, df_trades.info())

    df_merged = pd.merge_asof(df_trades, df_bid_ask, on='Time', direction='backward')
    df_merged.drop(columns = ['Unnamed: 0_x', ' TickAttriBidAsk', ' Unreported',' AskPastHigh','Unnamed: 0_y', 
    ' TickAttribLast'], inplace=True)
    df_merged['price_diff_bid']=np.abs(df_merged[' Price']-df_merged[' PriceBid'])
    df_merged['price_diff_ask']=np.abs(df_merged[' Price']-df_merged[' PriceAsk'])
    df_merged['closer_NBBO']=np.min(df_merged[['price_diff_ask', 'price_diff_bid']], axis =1)
    df_merged['weight_NBBO'] = df_merged[' Size'] *df_merged['closer_NBBO']
    return df_merged








#print('merged', df_agg.columns, df_agg)
    df_agg.to_clipboard()