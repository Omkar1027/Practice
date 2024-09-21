import pandas as pd

# CSV

marksCsv = pd.read_csv('FDS/MARKS_EXP4.csv')
print("Original Data:\n", marksCsv)

# no headers
marks_no_header = pd.read_csv('FDS/MARKS_EXP4.csv', header=None)
print( marks_no_header)

# Custom headers
custom_headers = ['Subject', 'Omkar_Marks', 'Kaustubh_Marks', 'Shreya_Marks', 'Parth_Marks']
marks_with_custom_headers = pd.read_csv('FDS/MARKS_EXP4.csv', names=custom_headers)
print(marks_with_custom_headers)

# Subject by headers
marks_with_index = pd.read_csv('FDS/MARKS_EXP4.csv', index_col='Subject')
print( marks_with_index)

# NA check
marks_with_na = pd.read_csv('FDS/MARKS_EXP4.csv', na_values=['91'])
print("\n'91' as NA:\n", marks_with_na)
print(pd.isnull(marks_with_na))

# Skipping rows
marks_skip_rows = pd.read_csv('FDS/MARKS_EXP4.csv', skiprows=[2])
print( marks_skip_rows)

# EXCEL

df = pd.read_excel('FDS/MARKS_XL.xlsx')
print("Original Data:\n", df)

# Extract specific columns
cols = ["Subject", "Omkar", "Kaustubh"]
df1 = pd.read_excel('FDS/MARKS_XL.xlsx', usecols=cols)
print(df1)

# Maximum marks
print(df[df.Omkar == df.Omkar.max()])

# Minimum marks
print(df[df.Omkar == df.Omkar.min()])

# Multiple sheets
df_sheets = pd.read_excel('FDS/MARKS_XL.xlsx', sheet_name=None)  
for sheet_name, sheet_data in df_sheets.items():
    print(f"Sheet: {sheet_name}\n", sheet_data)
