# week 9 pandas.py
import pandas as import pd
import numpy as np

def sep():
    print("________________________")

s = pd.Series(data=5, index=["a", "b", "c", "d", "e"])
print(s)
sep()
s = pd.Series(data=np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s)
sep()
s = pd.Series(data=np.random.randn(5))
print(s)
sep()

data = {'a':3.2, 'b':1, 'c':1.0, 'd':10, 'e':5}
s = pd.Series(data)
print(s)
# series like dictionary, single-level
sep()

print('a' in s) #true
print('z' in s) #false
print(s['a'])
sep()
print(s.sum())

sep()
# add 1 to each value
print(s+1)
print(s*2)
s2 = pd.Series(data=np.random.randn(5))
s3 = pd.Series(data=np.random.randn(10))
print(s2+s3)
sep()

data = {'a':3.2, 'b':1, 'c':"1.0", 'd':10, 'e':5}
s = pd.Series(data)
print(s)
#object

sep()
s = pd.Series(data=data, index['a','e'])
print(s)
data={
    'studentid':['a','b','c','d','e'],
    'gender':['m','f','m','f','m'],
    'score':[80,70,60,95,87]
}
dt = pd.DataFrame(data)
print(df)
df.set_index(['studentid'], inplace =True)
print(df)
# first 2 rows
print(df.head(2))
print(df.tail(2))
sep()

print(df['gender'])
print(df.gender) # name , type

print(df.loc['e'])

#select row
print(df.iloc[4]),
# slice row df[n:m]
print(df.df[:2])

df = pd.read_csv('pokemon.csv', index_col='#')
print(df.head())
