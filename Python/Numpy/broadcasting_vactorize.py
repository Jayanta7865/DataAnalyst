#Broadcasting:- in NumPy is a mechanism that allows arithmetic
# operations on arrays of different shapes by automatically expanding 
# the smaller array to match the larger one.

# | Feature | Vectorization           | Broadcasting          |
# | ------- | ----------------------- | --------------------- |
# | Meaning | Operation on full array | Shape adjustment      |
# | Purpose | Speed & efficiency      | Compatibility         |
# | Input   | Same size arrays        | Different size arrays |
# | Example | `a + b`                 | `a + 10`              |
# | Role    | Executes operation      | Prepares arrays       |


import numpy as np
prices=np.array([100,200,350,400])
discount=10
after_dis=prices-(prices*10/100)
print(after_dis)


arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([10,11,12])
print(arr1+arr2)

arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[10,11,12],[1,2,3]])
print(arr1+arr2)

##scaler brodcasting:Scalar broadcasting means applying a single value
#  (scalar) to every element of an array automatically.
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1*10)

##error
# ValueError: operands could not be broadcast together with shapes (2,3) (2,) 
# arr1=np.array([[1,2,3],[4,5,6]]) # (2,3)
# arr2=np.array([10,11]) #(2,)  
# print(arr1+arr2)

# Create a NumPy array of shape (3, 3) filled with random integers.
#  Add a 1D array of shape (3,) to each row of the 2D array using broadcasting.
##creat own random matrix 
matrix=np.random.randint(1,10,size=(3,3))
arr=np.array([10,20,30])
add=matrix+arr
print(matrix)
print(add)

# 2. Create a NumPy array of shape (4, 4) filled with random integers.
#  Subtract a 1D array of shape (4,) from each column of the 2D array using broadcasting.
random_arr=np.random.randint(10,20,size=(4,4))
sub_arr=np.array([1,2,3,4])
after_sub=(random_arr-sub_arr.reshape(4,1))
print(random_arr)
print(after_sub)


##vectirization
#Vectorization means performing operations on entire arrays at once 
# instead of using loops.

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)   # vectorization