import pandas as pd

pets = pd.DataFrame({'cat':[2,3,4], 'dog':[3,4,5]})
print (pets)
wild = pd.DataFrame({'cat':[1,2,3], 'dog':[6,7,8]})
print(wild)
human = pd.DataFrame({'cat':[1], 'dog':[1]})
print(human)
l = [pets, wild, human]
for o in l:
    df = pd.concat(l, axis = 1)
print (df)
