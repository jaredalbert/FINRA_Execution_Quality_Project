import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


df_agg = pd.read_csv('aggregated_data.csv')


df_groupby_weighted = df_agg.groupby(' Exchange')['weight_NBBO'].agg(['sum', 'count'])
print('df_groupby_weighted', df_groupby_weighted)
df_groupby_volume= df_agg.groupby(' Exchange')[' Size'].agg(['sum'])
print('df_groupby_volume',df_groupby_volume)

df_for_hist=pd.merge(df_groupby_weighted, df_groupby_volume, on=' Exchange')

df_for_hist['improvement_off_NBBO'] = df_for_hist['sum_x']/df_for_hist['sum_y']
df_for_hist.reset_index(inplace=True)
df_for_hist.sort_values(by='improvement_off_NBBO', ascending=True, inplace=True)
df_for_hist['width']=np.round(df_for_hist['sum_x']/np.max(df_for_hist['sum_x']),3)
w = list(np.round(np.linspace(.1,.99,16),3))
w2=[0.1, 0.159, 0.219, 0.278, 0.337, 0.397, 0.456, 0.515, 0.575, 0.634, 0.693, 0.753, 0.812, 0.871, 0.931, 0.99]
w3 = [float(i) for i in w2]
w4= [.1, .2, .3, .4, .5, .6, .7, .8, .9, .1, .2, .3, .4, .5, .4, .4]
print ('df_for hist: ', df_for_hist)
df_for_hist.to_csv('study_output.csv')


fig = plt.figure()
ax = fig.add_subplot(111)
colors = ['b','b','b','b','r','b','b','b','b','b','b','b','b','b','b']
ax.bar(x=df_for_hist[' Exchange'], height=df_for_hist['improvement_off_NBBO'],
    width=df_for_hist['width'], color=colors)
plt.title('Price Improvement by Exchange. Width represents the volume on that exchange', wrap = True)
plt.xlabel('Exchange')
plt.xticks(rotation=90)
plt.ylabel('Price Better than NBB or NBO')
plt.text(10,10, 'Width represents the volume on that exchange')
#df_for_hist.plot.bar(x=' Exchange', y='improvement_off_NBBO', colors = ['b','b','b','b','r','b','b','b','b','b','b','b','b','b','b'])
#df_for_hist.plot.bar(x=' Exchange', y='sum_y')
plt.show()