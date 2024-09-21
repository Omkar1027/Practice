import pandas as pd
import re

data = {'Omkar': 'omkarkadam532@gmail.com', 'Kaustubh': 'kk@ves.ac.in','Parth': 'parthb@yahoo.com', 'Atharv': 'ab@ves.ac.in'}

data = pd.Series(data)
print("Original Data:\n", data, "\n")

# to check null values
print("Null Values Check:\n", data.isnull(), "\n")

# some basic functions
print("Contains 'ves.ac.in':\n", data.str.contains('ves.ac.in'), "\n")
print("First 5 Characters:\n", data.str[:5], "\n")

# strip
data_stripped = data.str.strip()
print("Stripped Data:\n", data_stripped, "\n")

# join
data_joined = data_stripped.str.join(' - ')
print("Joined Data:\n", data_joined, "\n")

# to count the data
data_count = data.str.count('a')
print("Count of 'a':\n", data_count, "\n")

# to replace the data
data_replaced = data.str.replace('gmail.com', 'example.com')
print("Replaced Data:\n", data_replaced, "\n")

# data to lower and upper
data_lower = data.str.lower()
print("Lowercase Data:\n", data_lower, "\n")
data_upper = data.str.upper()
print("Uppercase Data:\n", data_upper, "\n")
