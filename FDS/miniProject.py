import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Scraped_Data.csv')

# Data Cleaning: Handling Missing Values (Removing rows with missing 'exactPrice' and 'sqftPrice')
df = df.dropna(subset=['exactPrice', 'sqftPrice'])

# Data Type Conversion: Converting 'postedOn' to datetime
df['postedOn'] = pd.to_datetime(df['postedOn'], format='%Y-%m-%d', errors='coerce')

# Ensure 'exactPrice' and 'sqftPrice' are numeric
df['exactPrice'] = pd.to_numeric(df['exactPrice'], errors='coerce')
df['sqftPrice'] = pd.to_numeric(df['sqftPrice'], errors='coerce')

# Optional: Removing rows with any invalid or negative prices
df = df[df['exactPrice'] > 0]
df = df[df['sqftPrice'] > 0]

# Feature Engineering: You can add custom features like price per room or aggregate by location, etc.
# Define price segments based on quantiles
df['priceSegment'] = pd.qcut(df['exactPrice'], q=[0, 0.25, 0.75, 1.0], labels=['Low', 'Mid', 'High'])

# Segment for sqftPrice
df['sqftPriceSegment'] = pd.qcut(df['sqftPrice'], q=[0, 0.25, 0.75, 1.0], labels=['Low', 'Mid', 'High'])

# Checking the segmentation
df[['exactPrice', 'priceSegment', 'sqftPrice', 'sqftPriceSegment']].head()
# Grouping by property type and calculating average prices
property_type_group = df.groupby('propertyType').agg({
    'exactPrice': ['mean', 'median'],
    'sqftPrice': ['mean', 'median']
}).reset_index()

property_type_group.columns = ['propertyType', 'AvgExactPrice', 'MedianExactPrice', 'AvgSqftPrice', 'MedianSqftPrice']

# Show the average prices for each property type
print(property_type_group)
# Grouping by locality (or another region-related column) and calculating average prices
region_group = df.groupby('locality').agg({
    'exactPrice': ['mean', 'median'],
    'sqftPrice': ['mean', 'median']
}).reset_index()

region_group.columns = ['locality', 'AvgExactPrice', 'MedianExactPrice', 'AvgSqftPrice', 'MedianSqftPrice']

# Show the average prices for each locality/region
print(region_group)
# Histogram for price segments
plt.figure(figsize=(10, 6))
sns.histplot(df['priceSegment'], discrete=True)
plt.title('Distribution of Properties by Price Segment')
plt.show()
# Boxplot for price distribution by property type
plt.figure(figsize=(10, 6))
sns.boxplot(x='propertyType', y='exactPrice', data=df)
plt.xticks(rotation=90)
plt.title('Price Distribution by Property Type')
plt.show()
# Heatmap for average price per square foot by region (locality)
pivot_table = df.pivot_table(values='sqftPrice', index='locality', aggfunc='mean')

plt.figure(figsize=(10, 12))
sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap of Average Price per Square Foot by Locality')
plt.show()
# Scatter plot of exactPrice vs sqftPrice by region
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sqftPrice', y='exactPrice', hue='locality', data=df)
plt.title('Relationship Between Sqft Price and Exact Price by Locality')
plt.show()
# Affordability metrics per locality
affordability_metrics = region_group.copy()
affordability_metrics['PriceToIncomeRatio'] = affordability_metrics['AvgExactPrice'] / 500000  # Assuming an average income of 500,000
affordability_metrics['AffordabilityIndex'] = affordability_metrics['PriceToIncomeRatio']

# Show affordability index
print(affordability_metrics[['locality', 'AffordabilityIndex']])
