import numpy as np

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#arr = np.random.randn(5, 4)
print("arr ", arr)
print('********************************************')

print("mean of arr", arr.mean())
print('********************************************')

print("sum of arr", arr.sum())
print('********************************************')

#Functions like mean and sum take an optional axis argument
#that computes the statistic over the given axis,

print("sum of arr", arr.sum(axis=0))
print('********************************************')

#arr.mean(1) means “compute mean across the columns” where
#arr.sum(0) means “compute sum down the rows.”

#cumsum - function returns the cumulative sum of the elements
#along the given axis
#cumprod - cumulative product

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print("arr 1D ", arr)
print('********************************************')

print("cumulative sum :", arr.cumsum())
print('********************************************')

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print("arr 2D ", arr)
print('********************************************')

print("cum sum row-wise :", arr.cumsum(axis=0))
print('********************************************')

#check - print(arr.cumprod(axis=1))


