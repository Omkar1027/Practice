import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample customer_info DataFrame
data = {
    'FullName': ['john doe', 'Jane SMITH', 'Alice Johnson', 'bob BROWN'],
    'Email': ['john.doe@gmail.com', 'jane.smith@yahoo.com', 'alice.johnson@hotmail.com', 'bob.brown@outlook.com'],
    'Phone': ['123-456-7890', '234-567-8901', '345-678-9012', '456-789-0123']
}

customer_info = pd.DataFrame(data)

# Splitting the 'FullName' into 'FirstName' and 'LastName'
customer_info[['FirstName', 'LastName']] = customer_info['FullName'].str.split(' ', n=1, expand=True)

print("Customer Info After Splitting Names:")
print(customer_info)

# Replace '.com' with '.org' in the 'Email' column
customer_info['Email'] = customer_info['Email'].str.replace('.com', '.org', regex=False)

print("\nCustomer Info After Replacing Email Domains:")
print(customer_info)

# Capitalize the first letter of each name in 'FirstName' and 'LastName'
customer_info['FirstName'] = customer_info['FirstName'].str.title()
customer_info['LastName'] = customer_info['LastName'].str.title()

print("\nCustomer Info After Capitalizing Names:")
print(customer_info)

# Extract domain names from the 'Email' column
customer_info['EmailDomain'] = customer_info['Email'].str.split('@').str[1]

# Count the frequency of each domain
domain_counts = customer_info['EmailDomain'].value_counts()

# Bar plot for email domain distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=domain_counts.index, y=domain_counts.values, palette="viridis")
plt.title('Distribution of Email Domains')
plt.ylabel('Number of Customers')
plt.xlabel('Email Domain')
plt.xticks(rotation=45)
plt.legend(title='Email Domain')
plt.show()
