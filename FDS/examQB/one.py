import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
sales_data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Product': ['A', 'B', 'A'],
    'Region': ['North', 'South', 'North'],
    'Sales': [200, 150, 300],
    'Quantity': [10, 15, 12]
}
sales_df = pd.DataFrame(sales_data)

# a) Group by Product and calculate total Sales and average Quantity
q1a = sales_df.groupby('Product').agg({'Sales': 'sum', 'Quantity': 'mean'})

# Plot total Sales by Product
q1a['Sales'].plot(kind='bar', title='Total Sales by Product', ylabel='Total Sales')
plt.show()

# b) Group by Product and Region, calculate total Sales and Quantity
q1b = sales_df.groupby(['Product', 'Region']).agg({'Sales': 'sum', 'Quantity': 'sum'})

# c) Convert Date to datetime and calculate monthly total Sales
sales_df['Date'] = pd.to_datetime(sales_df['Date'])
q1c = sales_df.groupby(sales_df['Date'].dt.to_period('M')).agg({'Sales': 'sum'})

# Plot monthly Sales
q1c.plot(kind='line', title='Monthly Total Sales', ylabel='Sales')
plt.show()