#one-dimensional array
#A 1D (one-dimensional) array in NumPy is a simple list-like structure
#  that stores elements in a single row.

import numpy as np
one_d=np.array([1,2,3,4,5])
print(one_d)

##2-d array
# A 2D (two-dimensional) array in NumPy is an array with rows and columns like a matrix or table.

two_d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_d)

##Multi-dimensional array
##A multi-dimensional array in NumPy is an array that has more than one dimension (axes).
# It can be 2D, 3D, or higher, and is used to store data in a structured format like tables, matrices, or even cubes.
import numpy as np
multi_d=np.array([[[1,2], [3,4]],
                 [[5,6], [7,8]]]
                 )
print(multi_d)

print(multi_d.ndim) # return the number of dimensional of array
print(multi_d.shape)
### creat array using pyhton list

arr=np.array([
    [[1,2],[5,6]],
    [[12,34],[23,45]]
    ])
print(type(arr))
print(arr)
print(arr.ndim)

#creat array with default values

##zero values
# syntax= np.zero(shape) 
zero_value=np.zeros((2,3,2)) 
print(zero_value)
print(zero_value.ndim)

#one values
# syntax= np.ones(shape) 
one_value=np.ones((3,3))
print(one_value)

## fill with default value
#syntex=np.full((shape),default value)
filled=np.full((2,2),3)
print(filled)

##creating sequance of numbers in numpy
# syntax=np.arange(star,stop,step)

sequance_arr=np.arange(1,10,2) 
print(sequance_arr) 

##creat identity matrix
#syntax=np.eye(shape)
# shape=int(input("Enter your identity matrix shape"))
identity_matrix=np.eye(3)
print(identity_matrix)

