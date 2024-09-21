import numpy as np

# CREATION AND RESHAPING

data=np.random.randn(3,2)
print("Random data: ",data,"\n")
marks=np.array([90,85.5,76.33,60.23])

#to check the datatype of the array
print(marks,marks.dtype,"\n")

#convert the marks to integers type
intMarks = marks.astype(np.int32)
print("Array and dtype of converted array: ",intMarks,intMarks.dtype,"\n")



# SLICING 

student1=np.array([90,85.5,76.33,60.23,32])
student2=np.array([80,93,60.22,85,32])

arr_slice = student1[:]  
arr_slice[0] = 64  
print("\nSlicing: ", student1)

# Check if the slice is a copy or a view
is_copy = not np.may_share_memory(arr_slice, student1)
print(is_copy)

# Creating a 2D array 
students = np.array([[90, 85.5, 76.33],
                     [60.23, 80, 93]])

# Accessing an individual element
element = students[1, 2] 
print("\nIndividual element: ", element)

# Extracting one row
row = students[0]  # Extracting the first row
print("\nExtracted row: ", row)

# Extracting one column
column = students[:, 1]  # Extracting the second column
print("\nExtracted column:", column)



#VECTORIZATION OPERATIONS

sub=student1-student2
print("Vectorized operation minus: ",sub)

#to compare the marks in two arrays
print("\nComaring marks: ",student1 > student2)