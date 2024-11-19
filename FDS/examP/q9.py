import pandas as pd
import re
import matplotlib as plt
import seaborn as sns

# Sample data for illustration
data = {
    'Emp_ID': ['E123', 'A456', 'B789'],
    'Department': ['HR', 'Sales', 'IT'],
    'Comments': ['Needs follow-up urgently', 'Employee is on leave', 'Onboarding process urgent']
}

# Creating the DataFrame
employee_data = pd.DataFrame(data)

# a) Extract any numerical ID from the Emp_ID column and create a new column called Numeric_ID
employee_data['Numeric_ID'] = employee_data['Emp_ID'].apply(lambda x: ''.join(re.findall(r'\d+', x)))

# b) Find all rows in Comments that contain the substring "urgent" (case-insensitive)
urgent_comments = employee_data[employee_data['Comments'].str.contains('urgent', case=False, na=False)]

# c) Replace any instances of the phrase "on leave" in Comments with "on vacation"
employee_data['Comments'] = employee_data['Comments'].str.replace('on leave', 'on vacation', case=False)

# Display the modified DataFrame and the urgent_comments DataFrame
print(employee_data)
print(urgent_comments)





# Setting the plot style
sns.set(style='whitegrid')

# Example: Bar chart showing the number of employees in each department
plt.figure(figsize=(10, 6))
sns.countplot(data=employee_data, x='Department')
plt.title('Number of Employees by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()

# Example: Pie chart for distribution of comments containing "urgent" vs. others
plt.figure(figsize=(8, 8))
urgent_flag = employee_data['Comments'].str.contains('urgent', case=False, na=False)
urgent_counts = urgent_flag.value_counts()
plt.pie(urgent_counts, labels=['Contains Urgent', 'Does Not Contain Urgent'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Urgent Comments Distribution')
plt.show()
