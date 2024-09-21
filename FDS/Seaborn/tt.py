import numpy as np

#Universal Functions: Fast Element-Wise Array Functions
#A universal function, or ufunc, is a function that performs
#element-wise operations on data in ndarrays

arr = np.arange(10)
print("arr :", arr)
print('*********************************************')

print("sqrt :",np.sqrt(arr))
print('*********************************************')

print("arr :", arr)
print('*********************************************')

print("exp :",np.exp(arr))
print('*********************************************')

#check the instruction to replace elements of array with sqrt)

#These are referred to as unary ufuncs.
#Others, such as add or maximum, take two arrays
#(thus, binary ufuncs) and return a single array as the result

x = np.random.randn(8)
print("x :",x)
print('*********************************************')

y = np.random.randn(8)
print("y :",y)
print('*********************************************')

print("maximum :",np.maximum(x, y))
print('*********************************************')

#a ufunc can return multiple arrays
#modf - returns the fractional and integral parts of a floating-point array
#method returns the fractional and integral parts of
#an input array, element-wise.

arr = np.random.randn(7) * 5
print("arr :",arr)
print('*********************************************')

remainder, whole_part = np.modf(arr)
print("whole_part :",whole_part)
print('*********************************************')

print("remainder :",remainder)
print('*********************************************')




      
