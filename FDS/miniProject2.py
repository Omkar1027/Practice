import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Scraped_Data.csv')

# Data Cleaning: Handling Missing Values (Removing rows with missing 'exactPrice' and 'sqftPrice')
df = df.dropna(subset=['exactPrice', 'sqftPrice'])

# Data Type Conversion: Converting 'postedOn' to datetime
df['postedOn'] = pd.to_datetime(df['postedOn'], errors='coerce', format='%Y-%m-%d')  # Adjust the format based on your data

# Ensure 'exactPrice' and 'sqftPrice' are numeric
df['exactPrice'] = pd.to_numeric(df['exactPrice'], errors='coerce')
df['sqftPrice'] = pd.to_numeric(df['sqftPrice'], errors='coerce')

# Optional: Removing rows with any invalid or negative prices
df = df[df['exactPrice'] > 0]
df = df[df['sqftPrice'] > 0]

# Define price segments based on quantiles
df['priceSegment'] = pd.qcut(df['exactPrice'], q=[0, 0.25, 0.75, 1.0], labels=['Low', 'Mid', 'High'])

# Group by locality (or any other region-based column) and calculate the mean prices
region_group = df.groupby('locality').agg({
    'sqftPrice': 'mean',
    'exactPrice': 'mean'
}).reset_index()

# Rename columns for clarity
region_group.columns = ['locality', 'AvgSqftPrice', 'AvgExactPrice']

# Simple heatmap for average price per square foot by locality
plt.figure(figsize=(10, 8))
sns.heatmap(region_group.pivot_table(values='AvgSqftPrice', index='locality'), annot=True, fmt=".2f", cmap='Blues')
plt.title('Average Price per Square Foot by Locality')
plt.show()

# Affordability metric: Affordability Index (simply using exact price)
region_group['AffordabilityIndex'] = 1 / region_group['AvgExactPrice']  # Higher index means more affordable

# Display simple affordability metrics
print(region_group[['locality', 'AvgExactPrice', 'AffordabilityIndex']])

# Scatter plot: Avg Sqft Price vs Avg Exact Price by locality
plt.figure(figsize=(8, 6))
sns.scatterplot(x='AvgSqftPrice', y='AvgExactPrice', data=region_group)
plt.title('Avg Sqft Price vs Avg Exact Price by Locality')
# plt.show()
