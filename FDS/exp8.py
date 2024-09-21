import numpy as np

#SORTING

marks=np.array([90, 85, 76, 60, 92, 88, 70])
marks.sort()
print("Sorted array: ",marks)

marks2D=[[90, 85, 76, 60],
         [92, 88, 70, 75],
         [80, 82, 90, 65],
         [78, 85, 88, 80]]
marks2D.sort()
print("\nSorted 2D array: ",marks2D)

arr=["z","d","a","b","d","z","b","o","i"]
print("\nUnique array: ",np.unique(arr))

#SEARCHING
names = [
    ['Omkar', 'Shreya', 'Parth', 'Atharv'],
    ['Omkar', 'Kaustubh', 'Yogesh', 'Atharv'],
    ['Omkar', 'Shreya', 'Omkar', 'Yogesh'],
    ['Atharv', 'Kaustubh', 'Shreya', 'Omkar']
]

print("\nSearching values:", np.in1d(names, ['Omkar', 'Yogesh', 'Atharv']))
