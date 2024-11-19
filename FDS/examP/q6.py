import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales_data DataFrame
data = {
    'Date': ['2024-01-05', '2024-01-15', '2024-02-20', '2024-02-25', '2024-03-10'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Furniture'],
    'Sales': [200, 150, 250, None, 300],
    'Discount': [10, 5, 15, None, 20]
}

sales_data = pd.DataFrame(data)

# Group by 'Category' and calculate mean and sum for 'Sales' and 'Discount'
grouped = sales_data.groupby('Category').agg(
    Sales_mean=('Sales', 'mean'),
    Sales_sum=('Sales', 'sum'),
    Discount_mean=('Discount', 'mean'),
    Discount_sum=('Discount', 'sum')
)

print(grouped)

# Fill missing 'Sales' values with the mean Sales of the corresponding Category
sales_data['Sales'] = sales_data.groupby('Category')['Sales'].transform(
    lambda x: x.fillna(x.mean())
)

print(sales_data)

# Convert 'Date' column to datetime
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Extract month and year from 'Date'
sales_data['Year'] = sales_data['Date'].dt.year
sales_data['Month'] = sales_data['Date'].dt.month

# Group by 'Year' and 'Month' to calculate total Sales per month
monthly_sales = sales_data.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

print(monthly_sales)

# Bar plot for mean Sales and Discount by Category
grouped.plot(kind='bar', y=['Sales_mean', 'Discount_mean'], figsize=(10, 6))
plt.title('Mean Sales and Discount by Category')
plt.ylabel('Value')
plt.show()

# Line plot for total Sales per month
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Sales', hue='Year', data=monthly_sales, marker='o')
plt.title('Total Sales per Month')
plt.ylabel('Total Sales')
plt.xlabel('Month')
plt.show()
