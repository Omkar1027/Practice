import pandas as pd
import matplotlib.pyplot as plt

# Sample customer_data DataFrame
customer_data = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104, 105],
    'OrderDate': ['2023-10-01', None, '2023-10-03', '2023-10-04', None],
    'Amount': [250.0, None, 300.0, None, 150.0],
    'Discount': [0.10, None, 0.15, None, None]
})

# Remove rows where more than two values are missing
customer_data = customer_data.dropna(thresh=2)

print("Data after removing rows with more than two missing values:")
print(customer_data)

# Fill missing Discount values with 0.05 (5%)
customer_data['Discount'] = customer_data['Discount'].fillna(0.05)

print("\nData after filling missing Discount values:")
print(customer_data)

# Forward fill for missing Amount values
customer_data['Amount'] = customer_data['Amount'].ffill()

print("\nData after forward filling missing Amount values:")
print(customer_data)

# Bar plot for Amount spent by each CustomerID
plt.figure(figsize=(10, 6))
plt.bar(customer_data['CustomerID'], customer_data['Amount'], color='green', label='Amount')
plt.xlabel('Customer ID')
plt.ylabel('Amount ($)')
plt.title('Amount Spent by Each Customer')
plt.xticks(customer_data['CustomerID'])
plt.legend()
plt.show()

# Line plot for Discounts
plt.figure(figsize=(10, 6))
plt.plot(customer_data['CustomerID'], customer_data['Discount'], marker='o', linestyle='-', color='blue', label='Discount Rate')
plt.xlabel('Customer ID')
plt.ylabel('Discount Rate')
plt.title('Discount Rates for Each Customer')
plt.xticks(customer_data['CustomerID'])
plt.legend()
plt.show()
