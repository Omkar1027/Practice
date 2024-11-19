import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample student_scores DataFrame with some missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Math_Score': [85, np.nan, 78, 92, np.nan],
    'Science_Score': [88, 76, np.nan, 85, 90],
    'English_Score': [np.nan, 79, 85, np.nan, 88]
}

student_scores = pd.DataFrame(data)

# Identify rows with missing values
missing_rows = student_scores[student_scores.isna().any(axis=1)]

print("Rows with missing values:")
print(missing_rows)

# Fill missing values in 'Math_Score' with the mean of 'Math_Score'
math_mean = student_scores['Math_Score'].mean()
student_scores['Math_Score'] = student_scores['Math_Score'].fillna(math_mean)

# Fill missing values in 'Science_Score' with the median of 'Science_Score'
science_median = student_scores['Science_Score'].median()
student_scores['Science_Score'] = student_scores['Science_Score'].fillna(science_median)

print("DataFrame after filling missing values for Math_Score and Science_Score:")
print(student_scores)

# Interpolate missing values in 'English_Score' using the linear method
student_scores['English_Score'] = student_scores['English_Score'].interpolate(method='linear')

print("DataFrame after interpolating missing values for English_Score:")
print(student_scores)

# Boxplot for the distribution of scores
plt.figure(figsize=(12, 6))
sns.boxplot(data=student_scores[['Math_Score', 'Science_Score', 'English_Score']])
plt.title('Distribution of Scores in Different Subjects')
plt.ylabel('Score')
plt.xlabel('Subjects')
plt.show()

# Bar plot showing average scores for each subject
average_scores = student_scores[['Math_Score', 'Science_Score', 'English_Score']].mean()

plt.figure(figsize=(10, 6))
sns.barplot(x=average_scores.index, y=average_scores.values, hue=average_scores.index, palette="magma", legend=False)
plt.title('Average Scores Across Subjects')
plt.ylabel('Average Score')
plt.xlabel('Subjects')
plt.show()
