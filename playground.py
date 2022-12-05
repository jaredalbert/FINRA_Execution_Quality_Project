import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

N = 5
ind = np.arange(N)
width = 0.5
vals = [1,2,3,4,5]
colors = ['r','b','b','b','b']
ax.barh(ind, vals, width, color=colors)

plt.show()

import matplotlib.pyplot as plt
 
#data
x = [1, 2, 3, 4, 5]
h = [10, 8, 12, 4, 7]
w = [0.8, 0.5, 0.2, 0.4, 0.9]
 
#bar plot
plt.bar(x, height = h, width = w)
 
plt.show()

""" import numpy as np

x = list(np.round(np.linspace(0.1,.99,16),3))
print(x) """

""" with open('symbols.txt', 'r') as f:
    x = [i for i in f.read().splitlines() if i]
print(x)     """
""" import pandas as pd

pets = pd.DataFrame({'cat':[2,3,4], 'dog':[3,4,5]})
print (pets)
wild = pd.DataFrame({'cat':[1,2,3], 'dog':[6,7,8]})
print(wild)
human = pd.DataFrame({'cat':[1], 'dog':[1]})
print(human)
l = [pets, wild, human]
for o in l:
    df = pd.concat(l, axis = 1)
print (df) """
