import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample product_details DataFrame
data = {
    'Product_ID': ['P001', 'P002', 'P003', 'P004'],
    'Category': [' Electronics ', ' Furniture', 'Appliances ', ' Clothing '],
    'Description': ['This is a premium quality product.', 'Affordable and durable.', 'Premium build with great features.', 'Stylish and comfortable.']
}

product_details = pd.DataFrame(data)

# Check if 'premium' exists in the 'Description' (case-insensitive) and create 'Is_Premium' column
product_details['Is_Premium'] = product_details['Description'].str.contains('premium', case=False)

print(product_details)

# Strip leading and trailing whitespace from 'Category' and 'Description'
product_details['Category'] = product_details['Category'].str.strip()
product_details['Description'] = product_details['Description'].str.strip()

print(product_details)

# Concatenate 'Category' and 'Product_ID' to form 'Product_Code' and convert to uppercase
product_details['Product_Code'] = (product_details['Category'] + '-' + product_details['Product_ID']).str.upper()

print(product_details)

# Count of premium vs. non-premium products
premium_counts = product_details['Is_Premium'].value_counts()

# Bar plot for premium and non-premium product distribution
plt.figure(figsize=(8, 5))
sns.barplot(x=premium_counts.index, y=premium_counts.values)
plt.title('Premium vs. Non-Premium Products')
plt.ylabel('Count')
plt.xlabel('Is Premium')
plt.xticks([0, 1], ['False', 'True'])  # Label the x-axis for better clarity
plt.show()
