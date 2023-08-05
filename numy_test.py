from numpy import *
arr=array([
    [2,8,5,9,9,75],
    [52,78,86,78,96,1]
]
     )
print(arr.dtype)
print(arr.shape)
print(arr.size)
arr3=arr.reshape(2,3,2)
print(arr3)

