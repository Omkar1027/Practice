import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for illustration
data = {
    'Department': ['HR', 'Sales', 'IT', 'HR', 'Sales', 'IT', 'Sales', 'HR', 'IT'],
    'Salary': [50000, 60000, 70000, 52000, 65000, 72000, 62000, 53000, 80000],
    'Age': [25, 30, 35, 28, 32, 40, 29, 27, 45],
    'Experience': [1, 5, 7, 2, 4, 8, 3, 1, 10]
}

# Creating the DataFrame
employee_data = pd.DataFrame(data)

# a) Group by Department and calculate mean, median, and standard deviation for Salary and Experience
salary_experience_stats = employee_data.groupby('Department')[['Salary', 'Experience']].agg(['mean', 'median', 'std']).reset_index()

# Flattening the MultiIndex columns for easier access
salary_experience_stats.columns = ['_'.join(col).strip() if type(col) is tuple else col for col in salary_experience_stats.columns]

print("Mean, Median, and Standard Deviation for Salary and Experience by Department:")
print(salary_experience_stats)

# b) Group by Department and Age, and find the minimum and maximum Salary within each group
salary_age_stats = employee_data.groupby(['Department', 'Age'])['Salary'].agg(['min', 'max']).reset_index()
print("\nMinimum and Maximum Salary by Department and Age:")
print(salary_age_stats)

# c) Calculate total and average Salary grouped by Department and Experience level
# Defining experience levels
bins = [0, 2, 5, 10]  # Example bins for Junior, Mid, Senior
labels = ['Junior', 'Mid', 'Senior']
employee_data['Experience_Level'] = pd.cut(employee_data['Experience'], bins=bins, labels=labels, right=False)

# Group by Department and Experience Level with observed=True to silence the FutureWarning
salary_experience_level = employee_data.groupby(['Department', 'Experience_Level'], observed=True)['Salary'].agg(['sum', 'mean']).reset_index()
print("\nTotal and Average Salary by Department and Experience Level:")
print(salary_experience_level)

# d) Display suitable graphs/plots/charts

# Setting the plot style
sns.set(style='whitegrid')

# 1. Bar plot of mean Salary and Experience by Department
plt.figure(figsize=(10, 6))
salary_experience_melt = salary_experience_stats[['Department_', 'Salary_mean', 'Experience_mean']].melt(id_vars='Department_', var_name='Metric', value_name='Mean Value')

sns.barplot(data=salary_experience_melt, x='Department_', y='Mean Value', hue='Metric')
plt.title('Mean Salary and Experience by Department')
plt.xlabel('Department')
plt.ylabel('Mean Value')
plt.legend(title='Metrics')
plt.show()

# 2. Bar plot of total Salary by Department and Experience Level
plt.figure(figsize=(10, 6))
sns.barplot(data=salary_experience_level, x='Department', y='sum', hue='Experience_Level')
plt.title('Total Salary by Department and Experience Level')
plt.xlabel('Department')
plt.ylabel('Total Salary')
plt.legend(title='Experience Level')
plt.show()
