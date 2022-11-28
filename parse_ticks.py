''''Retrieves the pickle object from the  
historicalTicksBidAsk method overloaded in the wrapper.py and loads that 
bid ask data into a Pandas Dataframe'''

import pickle
from collections import defaultdict
import pandas as pd

def parse_ticks():

    with open ('bid_ask.pk', 'rb') as f:
        vars = pickle.load(f) 

    vars_list = list(vars)
    l = []
    d={}
    for item in vars_list:
        x = str(item).split(',')
        for field in x:
            y = list(str(field).split(':'))
            #print (type(y[0]),type(([1])))
            if y[0] not in d.keys():
                d[y[0]] = (y[1])
            else:
                d[y[0]]+=((y[1]))


        
    new_d = {k:v.split(' ') for k, v in d.items()}        
    df = pd.DataFrame.from_dict(new_d, orient = 'columns')
    df.to_csv('df_bid_ask.csv')
    print ('parse_ticks: ', df)

    with open ('trades.pk', 'rb') as f:
        vars = pickle.load(f) 

    vars_list = list(vars)
    l = []
    d={}
    for item in vars_list:
        x = str(item).split(',')
        for field in x:
            y = list(str(field).split(':'))
            print (type(y[0]),type(([1])))
            if y[0] not in d.keys():
                d[y[0]] = (y[1])
            else:
                d[y[0]]+=((y[1]))


        
    new_d = {k:v.split(' ') for k, v in d.items()}        
    df = pd.DataFrame.from_dict(new_d, orient = 'columns')
    df.to_csv('df_trades.csv')
    print (df)
    
if __name__ == '__main__':
    parse_ticks()

