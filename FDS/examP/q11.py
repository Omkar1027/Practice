import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for illustration
data = {
    'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown'],
    'Role': ['  manager ', 'Sales representative', 'director'],
    'Office_Location': ['New York City', 'San Francisco', 'Los Angeles']
}

# Creating the DataFrame
sales_team = pd.DataFrame(data)

# a) Extract the first letter from each word in Office_Location and create an abbreviation
sales_team['Location_Abbr'] = sales_team['Office_Location'].str.split().str[0]
print(sales_team)

# b) Standardize all roles to uppercase and remove any whitespace
sales_team['Role'] = sales_team['Role'].str.upper().str.strip()
print(sales_team)

# c) Concatenate Name and Role into a new column called Name_with_Role
sales_team['Name_with_Role'] = sales_team['Name'] + ' - ' + sales_team['Role']
print(sales_team)

# Example: Bar chart showing the number of people at each Office_Location
plt.figure(figsize=(10, 6))
sns.countplot(data=sales_team, x='Office_Location')
plt.title('Number of Employees by Office Location')
plt.xlabel('Office Location')
plt.ylabel('Number of Employees')
plt.show()

