import pandas as pd


string_data = pd.Series(['aardvark', 'artichoke', pd.NA, 'avocado'])

#print(string_data)

#print(string_data.isnull())
#print('************************************************************')

data = pd.Series([1, pd.NA, 3.5, pd.NA, 7])
print(data)
print(data.dropna())
#print('************************************************************')

data = pd.DataFrame([[1., 6.5, 3.],[1., pd.NA, pd.NA],[1, pd.NA, pd.NA],[1, 6.5, 3.]])

print(data)
print('************************************************************')

cleaned = data.dropna()
print(cleaned)
# print('************************************************************')

# print(data.dropna(how='all'))
# print('************************************************************')

print(data.dropna(thresh=1))
print('************************************************************')

# print(data.dropna(axis=1, how='all'))
# print('************************************************************')

#understand data.dropna(thresh=2)



# pd.set_option('future.no_silent_downcasting', True)
print(data.fillna(0))

#understand dataframe.fillna(value, method, axis, inplace, limit, downcast)
#understand data.fillna({1: 0.5, 2: 0})
#understand .ffill and .bfill

_ooo = data.fillna(0, inplace=True)
print(_ooo)

