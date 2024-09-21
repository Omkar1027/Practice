import pandas as pd

# CSV

marksCsv = pd.read_csv('FDS/MARKS_EXP4.csv')
print("Original Data:\n", marksCsv, "\n")

# Load CSV without headers
marks_no_header = pd.read_csv('FDS/MARKS_EXP4.csv', header=None)
print("Data Without Headers:\n", marks_no_header, "\n")

# Custom headers
custom_headers = ['Subject', 'Omkar_Marks', 'Kaustubh_Marks', 'Shreya_Marks', 'Parth_Marks']
marks_with_custom_headers = pd.read_csv('FDS/MARKS_EXP4.csv', names=custom_headers)
print("Data With Custom Headers:\n", marks_with_custom_headers, "\n")

#Subject as index
marks_with_index = pd.read_csv('FDS/MARKS_EXP4.csv', index_col='Subject')
print("Data With Subject Index:\n", marks_with_index, "\n")

# Check for NA values
marks_with_na = pd.read_csv('FDS/MARKS_EXP4.csv', na_values=['91'])
print("\n'91' Treated as NA:\n", marks_with_na, "\n")
print("NA Check:\n", pd.isnull(marks_with_na), "\n")

# Skip specific rows
marks_skip_rows = pd.read_csv('FDS/MARKS_EXP4.csv', skiprows=[2])
print("Data After Skipping Rows:\n", marks_skip_rows, "\n")

# EXCEL

# Load original Excel data
df = pd.read_excel('FDS/MARKS_XL.xlsx')
print("Original Excel Data:\n", df, "\n")

# Extract specific columns from Excel
cols = ["Subject", "Omkar", "Kaustubh"]
df1 = pd.read_excel('FDS/MARKS_XL.xlsx', usecols=cols)
print("Extracted Columns:\n", df1, "\n")

# Maximum marks 
print("Maximum Marks in Omkar's Column:\n", df[df.Omkar == df.Omkar.max()], "\n")

# Minimum marks
print("Minimum Marks in Omkar's Column:\n", df[df.Omkar == df.Omkar.min()], "\n")

# Load multiple sheets from Excel
df_sheets = pd.read_excel('FDS/MARKS_XL.xlsx', sheet_name=None)  
for sheet_name, sheet_data in df_sheets.items():
    print(f"Sheet: {sheet_name}\n", sheet_data, "\n")
