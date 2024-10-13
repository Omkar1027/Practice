import pandas as pd

# Student data
student_data = [
    {"Name": "Sagar", "Surname": "Jadhav", "Age": 24},
    {"Name": "Aary", "Surname": "Jain", "Age": 25},
    {"Name": "Guneet", "Surname": "Jaisinghania", "Age": 26},
    {"Name": "Omkar", "Surname": "Kadam", "Age": 27},
    {"Name": "Lakhan", "Surname": "Karani", "Age": 28},
    # ... add remaining student data
]

# Create a DataFrame from the data
df = pd.DataFrame(student_data)

# Save the DataFrame to a CSV file
df.to_csv("student_data.csv", index=False)

print("CSV file created successfully!")