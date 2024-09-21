import pandas as pd

marks = [ 
    ["Math", 85, pd.NA, 78, 92],
    ["Physics", 90, 75, pd.NA, 88],
    ["Chemistry", pd.NA, 80, 67, pd.NA],
    ["Biology", 92, 89, 94, pd.NA],
    ["English", 88, pd.NA, 82, 90]
]

columns = ["Subject", "Omkar", "Kaustubh", "Shreya", "Parth"]

records = pd.DataFrame(marks, columns=columns)

print(records)

#to clean the data 
clean=records.dropna()
print(clean)

#to fill the na values by 0
clean=records.fillna(0)
print(clean)

#sum aggregrate function
print(clean.sum())

df = pd.DataFrame([   
    ['AIDS', 9, 4, 8, 9], 
    ['AIDS', 8, 10, 7, 6], 
    ['IT', 7, 6, 8, 5]
], columns=['class', 'Maths', 'English', 'Science', 'History'])

#to groupby the marks by branch
group=df.groupby('class')
print(group.get_group('AIDS'))

#to count the data entries in the group
print(group.count())