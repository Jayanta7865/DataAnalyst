# # Module: NumPy Assignments
# ## Lesson: NumPy
# ### Assignment 1: Array Creation and Manipulation

# 1. Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. Replace all the elements in the third column with 1.
import numpy as np
arr=np.random.randint(1,21,size=(5,5))
arr[:,2]=1
print("After Replace all the elements in the third column with 1\n",arr)

# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.
matrix=np.random.randint(1,17,size=(4,4))
print("4,4 matrix is:\n",matrix)
np.fill_diagonal(matrix,0)
print("Replace the diagonal elements with 0:\n",matrix)
# ### Assignment 2: Array Indexing and Slicing

# 1. Create a NumPy array of shape (6, 6) with values from 1 to 36. Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.
six_six=np.arange(1,37).reshape(6,6)
print("6,6 matrix\n",six_six)
a=six_six[2:5,1:4]
print("After slicing\n",a)

# 2. Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.
five_five=np.random.randint(1,21,size=(5,5))
print("5,5 matrix:\n",five_five)
border_element=np.concatenate((five_five[0,:],five_five[-1,:],five_five[1:-1,0],five_five[1:-1,-1]))
print("after slicing\n",border_element)
# ### Assignment 3: Array Operations

# 1. Create two NumPy arrays of shape (3, 4) filled with random integers. Perform element-wise addition, subtraction, multiplication, and division.
three_four=np.random.randint(1,21,size=(3,4))
print("3,4 matrix:\n",three_four)
three_four2=np.random.randint(1,21,size=(3,4))
print("3,4 next matrix\n",three_four2)
print("After sum element wise:\n",three_four+three_four2)
# 2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Compute the row-wise and column-wise sum.
four_four=np.arange(1,17).reshape(4,4)
print("4,4 matrix:\n",four_four)
row_wise=np.sum(four_four,axis=0)
print("Row wise sum:\n",row_wise)
colum_wise=np.sum(four_four,axis=1)
print("Column wise sum:\n",colum_wise)
# ### Assignment 4: Statistical Operations

# 1. Create a NumPy array of shape (5, 5) filled with random integers. Compute the mean, median, standard deviation, and variance of the array.
random_matrix=np.random.randint(1,25,size=(5,5))
print("Random matrix:\n",random_matrix)
print("Mean:",np.mean(random_matrix))
print("median:",np.median(random_matrix))
print("standard deviation:",np.std(random_matrix))
print("variance:",np.var(random_matrix))
# 2. Create a NumPy array of shape (3, 3) with values from 1 to 9. Normalize the array (i.e., scale the values to have a mean of 0 and a standard deviation of 1).
three_three1=np.arange(1,10).reshape(3,3)
print("3,3 matrix:",three_three1)
men=np.mean(three_three1)
std=np.std(three_three1)
normalized_array=(three_three1-men)/std
print("Normalized array:\n",normalized_array)

# ### Assignment 5: Broadcasting

# 1. Create a NumPy array of shape (3, 3) filled with random integers. Add a 1D array of shape (3,) to each row of the 2D array using broadcasting.
three_three=np.random.randint(1,10,size=(3,3))
print("3,3 matrix:\n",three_three)
oned_arr=np.array([10,20,30])
print("one d array:\n",oned_arr)
print("After brodcastong\n",three_three+oned_arr) 
# 2. Create a NumPy array of shape (4, 4) filled with random integers. Subtract a 1D array of shape (4,) from each column of the 2D array using broadcasting.
four_matrix=np.random.randint(1,17,size=(4,4))
print("4,4 matrix:\n",four_matrix)
one_d=np.array([10,20,30,40]).reshape(4,1)
print("One d array:\n",one_d)
print("After brodcasting\n",four_matrix-one_d)
# ### Assignment 6: Linear Algebra

# 1. Create a NumPy array of shape (3, 3) representing a matrix. Compute its determinant, inverse, and eigenvalues.
three_mat=np.random.randint(1,10,size=(3,3))
print("3,3 matrix:\n",three_mat)
det=(np.linalg.det(three_mat))
print("Determinate:",det)
inver=np.linalg.inv(three_mat)
print("Inverse:",inver)
eigen=np.linalg.eigvals(three_mat)
print("Eigen value:",eigen)
# 2. Create two NumPy arrays of shape (2, 3) and (3, 2). Perform matrix multiplication on these arrays.
first=np.arange(1,7).reshape(2,3)
print("First array:\n",first)
second=np.arange(1,7).reshape(3,2)
print("First array:\n",second)
mul=np.dot(first,second)
print("Matrix maltiplication:\n",mul)
# ### Assignment 7: Advanced Array Manipulation

# 1. Create a NumPy array of shape (3, 3) with values from 1 to 9. Reshape the array to shape (1, 9) and then to shape (9, 1).
three_three_matrix=np.arange(1,10).reshape(3,3)
print("Matrix is:\n",three_three_matrix)
re_sh=three_three_matrix.reshape(1,9)
print("1,9:\n",re_sh)
re_sh2=three_three_matrix.reshape(9,1)
print("9,1:\n",re_sh2)
# 2. Create a NumPy array of shape (5, 5) filled with random integers. Flatten the array and then reshape it back to (5, 5).
five_mat=np.arange(1,26).reshape(5,5)
print("5,5:\n",five_mat)
flat=five_mat.flatten()
print("After Flatten\n",flat)
re_shape=flat.reshape(5,5)
print("After reshape 5,5\n",re_shape)

# ### Assignment 8: Fancy Indexing and Boolean Indexing

# 1. Create a NumPy array of shape (5, 5) filled with random integers. Use fancy indexing to extract the elements at the corners of the array.
# 2. Create a NumPy array of shape (4, 4) filled with random integers. Use boolean indexing to set all elements greater than 10 to 10.

# ### Assignment 9: Structured Arrays

# 1. Create a structured array with fields 'name' (string), 'age' (integer), and 'weight' (float). Add some data and sort the array by age.
# 2. Create a structured array with fields 'x' and 'y' (both integers). Add some data and compute the Euclidean distance between each pair of points.

# ### Assignment 10: Masked Arrays

# 1. Create a masked array of shape (4, 4) with random integers and mask the elements greater than 10. Compute the sum of the unmasked elements.
# 2. Create a masked array of shape (3, 3) with random integers and mask the diagonal elements. Replace the masked elements with the mean of the unmasked elements.
