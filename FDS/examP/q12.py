import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame for demonstration
data = {
    'Order_ID': [1, 2, 3, 4],
    'Product_Name': [' Widget A ', 'Gadget B', '   Device C ', '  Widget D  '],
    'Customer_Comments': ['Great product, love the discount', 
                          ' ', 
                          'Excellent value with discount',
                          'Fast shipping, great discount!  ']
}

order_data = pd.DataFrame(data)

# a) Identify and remove any extra whitespace in Product_Name and Customer_Comments
order_data['Product_Name'] = order_data['Product_Name'].str.strip()
order_data['Customer_Comments'] = order_data['Customer_Comments'].str.strip()

# b) Replace occurrences of the word “discount” in Customer_Comments with “promo”
order_data['Customer_Comments'] = order_data['Customer_Comments'].str.replace('discount', 'promo', case=False)

# c) Extract the first word from each Customer_Comments entry and store it in a new column called First_Word
order_data['First_Word'] = order_data['Customer_Comments'].str.split().str[0].str.title()

# Display the modified DataFrame
print(order_data)

# d) Display suitable graphs/plots/charts wherever necessary
# For example, we could visualize the counts of the first words
first_word_counts = order_data['First_Word'].value_counts()

# Plotting
plt.figure(figsize=(10, 6))
first_word_counts.plot(kind='bar', color='skyblue')
plt.title('Count of First Words in Customer Comments')
plt.xlabel('First Words')
plt.ylabel('Counts')
#plt.xticks(rotation=45)
#plt.grid(axis='y')
#plt.tight_layout()
plt.show()
