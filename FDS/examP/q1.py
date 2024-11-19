import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales DataFrame
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-03', '2024-02-01', '2024-02-02'],
    'Product': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Sales': [200, 150, 300, 250, 400, 350],
    'Quantity': [2, 1, 4, 3, 5, 4]
}

sales = pd.DataFrame(data)

# Group by 'Product' and calculate total Sales and average Quantity
product_summary = sales.groupby('Product').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Quantity=('Quantity', 'mean')
).reset_index()

print("Total Sales and Average Quantity by Product:")
print(product_summary)

# Group by 'Product' and 'Region' and calculate total Sales and Quantity
region_product_summary = sales.groupby(['Product', 'Region']).agg(
    Total_Sales=('Sales', 'sum'),
    Total_Quantity=('Quantity', 'sum')
).reset_index()

print("\nTotal Sales and Quantity by Product and Region:")
print(region_product_summary)


# Convert 'Date' to datetime
sales['Date'] = pd.to_datetime(sales['Date'])

# Group by Date and calculate monthly total Sales
monthly_sales = sales.groupby(sales['Date'].dt.to_period('M')).agg(
    Total_Sales=('Sales', 'sum')
).reset_index()

print("\nMonthly Total Sales:")
print(monthly_sales)

# Bar plot for total Sales and average Quantity by Product
plt.figure(figsize=(12, 6))
sns.barplot(x='Product', y='Total_Sales', data=product_summary, color='skyblue', label='Total Sales')
sns.barplot(x='Product', y='Average_Quantity', data=product_summary, color='salmon', alpha=0.5, label='Average Quantity')
plt.title('Total Sales and Average Quantity by Product')
plt.ylabel('Value')
plt.xlabel('Product')
plt.legend()
plt.show()

# Line plot for monthly total Sales
monthly_sales['Date'] = monthly_sales['Date'].dt.to_timestamp()  # Convert Period to Timestamp for plotting
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Total_Sales', data=monthly_sales, marker='o')
plt.title('Monthly Total Sales')
plt.ylabel('Total Sales')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.show()
