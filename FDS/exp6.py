import numpy as np

#Matrix operations on forecast 

Monday=np.array([90,85.5,76.33,60.23,32])
Tuesday=np.array([80,93,60.22,85,32])
Wednesday=np.array([87,45,89,45,68])
Thursday=np.array([85,54.55,78.9,54.99,98])
Friday=np.array([98,45.7,97,65.87,55])

# Addition
add = Monday + Friday 
print("\nMatrix Addition:\n", add)

# Subtraction
sub = Monday - Tuesday
print("\nMatrix Subtraction:\n", sub)

# Multiplication
mul = Monday * Tuesday
print("\nMatrix Multiplication (element-wise):\n", mul)

#Inversion
allDays = np.array([Monday, Tuesday, Wednesday, Thursday, Friday])
inv_matrix = np.linalg.inv(allDays)
print("Inverse Matrix:\n", inv_matrix)

