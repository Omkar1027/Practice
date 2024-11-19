import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for illustration
data = {
    'Response_ID': [1, 2, 3, 4],
    'Respondent_Name': ['John Doe', 'Jane Smith', 'Emily Davis', 'Michael Brown'],
    'Feedback': [
        "The SERVICE was great. I really liked the service provided.",
        "Excellent customer SERVICE. Service could not be better.",
        "Good SERVICE, but there were some issues.",
        "Service was ok. Too many SERVICE interruptions!"
    ]
}

# Creating the DataFrame
survey_data = pd.DataFrame(data)

# a) Create a new column called Initials from Respondent_Name
survey_data['Initials'] = survey_data['Respondent_Name'].apply(lambda x: ''.join([name[0].upper() for name in x.split()]))
print(survey_data[['Respondent_Name', 'Initials']])

# b) Convert Feedback to lowercase and count occurrences of the word "service"
survey_data['Feedback'] = survey_data['Feedback'].str.lower()
survey_data['Service_Count'] = survey_data['Feedback'].str.count(r'\bservice\b')
print(survey_data[['Feedback', 'Service_Count']])

# c) Replace multiple spaces with a single space in Feedback
survey_data['Feedback'] = survey_data['Feedback'].replace(r'\s+', ' ', regex=True)
print(survey_data['Feedback'])

# d) Visualization

# 1. Bar plot: Count of "service" mentions by respondent
plt.figure(figsize=(8, 5))
sns.barplot(x='Respondent_Name', y='Service_Count', data=survey_data, palette='viridis')
plt.title('Count of "Service" Mentions by Respondent')
plt.xlabel('Respondent')
plt.ylabel('Service Count')
plt.xticks(rotation=45)
plt.show()

# 2. Pie chart: Distribution of total "service" mentions
service_distribution = survey_data.groupby('Respondent_Name')['Service_Count'].sum()
plt.figure(figsize=(6, 6))
service_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Distribution of "Service" Mentions')
plt.ylabel('')  # Hide the y-label
plt.show()
