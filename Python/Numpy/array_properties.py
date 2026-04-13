import numpy as np

##when we use shape, size, ndim in numpy

##Shape:- return number of row and column in an array

arr=np.array([
    [[1,2]],[[4,5]],
    [[7,8]],[[10,11]]
    ])
print(arr)
print(arr.shape)

##Size:- return number of element in an array

print(arr.size)

##ndim:- return number of dimensional an array

print(arr.ndim)

## .dtype:-check data type of element
 
arr1=np.array([1,2,3,38])
print(arr1.dtype)

##astype:- change data type in an given array
#syntax=array_name.astype(new_type)

float_arr=arr1.astype(str)
print(float_arr)
print(float_arr.dtype)

##mathematical operation
#like- +,-,*,/,//,**,%

arr2=np.array([1,2,3,4])

print(arr2 + 5)
print(arr2 * 5)
print(arr2 / 5)
print(arr2 ** 2)
print(arr2 // 2)
print(arr2 % 3)

##Aggregation function
#“Aggregation functions in NumPy are used to perform summary operations
#  like sum, mean, max, and min,veriance,standard deviation on array 
# elements to produce a single result.”
import numpy as np

arr=np.array([10,20,30,40,50,60])
print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))
print(np.median(arr))


