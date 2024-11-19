import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a simple DataFrame
weather_data = pd.DataFrame({
    'Date': ['2024-10-01', '2024-10-02', None, '2024-10-04', '2024-10-05'],
    'Temperature': [25, None, 30, 28, None],
    'Humidity': [80, None, 60, None, 70],
    
    'WindSpeed': [10, 12, 14, 11, 10]
})

# a) Detect missing values and calculate percentages
print(weather_data.isnull().mean() * 100)

# b) Remove rows with missing Date and fill missing Temperature with backward fill
weather_data = weather_data.dropna(subset=['Date'])
weather_data['Temperature'] = weather_data['Temperature'].bfill()

# c) Fill missing Humidity with the average of the day of the week
weather_data['Date'] = pd.to_datetime(weather_data['Date'])
weather_data['DayOfWeek'] = weather_data['Date'].dt.dayofweek
avg_humidity = weather_data.groupby('DayOfWeek')['Humidity'].transform('mean')
weather_data['Humidity'] = weather_data['Humidity'].fillna(avg_humidity)

# d) Plot a heatmap to show missing data
sns.heatmap(weather_data.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()
