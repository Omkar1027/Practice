import numpy as np

# Individual arrays
Monday = np.array([90, 85.5, 76.33, 60.23, 32])
Tuesday = np.array([80, 93, 60.22, 85, 32])
Wednesday = np.array([87, 45, 89, 45, 68, 88.55])
Thursday = np.array([85, 54.55, 78.9, 54.99, 98])
Friday = np.array([98, 45.7, 97, 65.87, 55])

# Find the maximum length
max_length = max(len(Monday), len(Tuesday), len(Wednesday), len(Thursday), len(Friday))

# Pad shorter arrays with NaN
Monday = np.pad(Monday, (0, max_length - len(Monday)), constant_values=np.nan)
Tuesday = np.pad(Tuesday, (0, max_length - len(Tuesday)), constant_values=np.nan)
Wednesday = np.pad(Wednesday, (0, max_length - len(Wednesday)), constant_values=np.nan)
Thursday = np.pad(Thursday, (0, max_length - len(Thursday)), constant_values=np.nan)
Friday = np.pad(Friday, (0, max_length - len(Friday)), constant_values=np.nan)

# Combining into a single NumPy array
combined = np.array([Monday, Tuesday, Wednesday, Thursday, Friday])

print("Combined Array:\n", combined)
