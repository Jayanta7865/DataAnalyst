##Reshaping:-Reshaping means changing the shape (dimensions) of 
# an array without changing its data.
#The number of elements before and after reshaping must be equal
##syntax=array.reshape(shape)


import numpy as np
arr=np.array([1,2,3,4,5,6])
# print(arr.reshape(3,3))
print(arr.reshape(2,3))
arr1=np.array([1,2,3,4,5,6,7,8,9])
print(arr1.reshape(3,3))


##reshape 2d and md to 1d
## we convert 2d and md to 1d using many process these are:-
# | Method      | Returns | Memory       |
# | ----------- | ------- | ------------ |
# | reshape(-1) | View    | Efficient    |
# | ravel()     | View    | Efficient    |
# | flatten()   | Copy    | Extra memory |

arr_3d=np.array([
   [ [1,2,3],
    [4,5,6]],
    [ [11,22,33],
    [44,55,66]],
])
print(arr_3d.reshape(-1)) #first process
print(arr_3d.ravel()) #second process
print(arr_3d.flatten()) #Third process