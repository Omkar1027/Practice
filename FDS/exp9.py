import numpy as np

# MATH FUNCTIONS

student1 = np.array([90, 85.5, 76.33, 60.23, 32])
student2 = np.array([80, 93, 60.22, 85, 32])
print("Maximum marks:", np.maximum(student1, student2), "\n")

# to extract integer part only
remainder, whole_part = np.modf(student1)
print(whole_part, "\n")
print(remainder, "\n")

all = np.array([[90, 85.5, 76.33, 60.23, 32], [80, 93, 60.22, 85, 32]])

# sum and mean
print("Mean of s1 marks:", student1.mean(), "\n")
print("Sum of s2 marks:", student2.sum(), "\n")
print("Median of s2 marks:", np.median(student2), "\n")
print("Cumulativeum sum :", all.cumsum(), "\n")

# Greater than
greater_than = student1 > student2
print("Greater than:", greater_than, "\n")

# Less than or equal to
less_than_equal = student1 <= student2
print("Less than or equal to:", less_than_equal, "\n")

# Equal
equal = student1 == student2
print("Equal:", equal, "\n")