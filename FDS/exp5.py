import pandas as pd
import re

data = {'Omkar': 'omkarkadam532@gmail.com', 'Kaustubh': 'kk@ves.ac.in','Parth': 'parthb@yahoo.com', 'Atharv': 'ab@ves.ac.in'}

data = pd.Series(data)
print(data)

# to check null values
print(data.isnull())

# some basic functions
print(data.str.contains('ves.ac.in'))
print(data.str[:5])

#strip
data_stripped = data.str.strip()
print(data_stripped)

# join
data_joined = data_stripped.str.join(' - ')
print(data_joined)

# to count the data
data_count = data.str.count('a')
print(data_count)

# to replace the data
data_replaced = data.str.replace('gmail.com', 'example.com')
print(data_replaced)

# data to lower and upper
data_lower = data.str.lower()
print(data_lower)
data_upper = data.str.upper()
print(data_upper)