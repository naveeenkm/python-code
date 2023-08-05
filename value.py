from array import *
arr=array('i',[1,2,8,7,6])
arr1=arr
print(arr,arr1)
if id(arr1)==id(arr):
    print(id(arr))
    print(id(arr1))
arr2=arr.copy()
if id(arr2)==id(arr):
    print(id(arr))
    print(id(arr2))
else:
    print(id(arr))
    print(id(arr2))