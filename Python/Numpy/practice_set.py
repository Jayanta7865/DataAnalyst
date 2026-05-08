# Create a NumPy array from 1 to 20
import numpy as np
arr=np.arange(1,21).reshape(4,5)
print("array from 1 to 20\n",arr)
# Create a 3×3 matrix with all zeros
arr2=np.zeros((3,3))
print("3×3 matrix with all zeros\n",arr2)
# Create a 4×4 identity matrix
identity_matrix=np.eye(4,4)
print("4×4 identity matrix\n",identity_matrix)
# Generate 10 random integers between 1–100
random=np.random.randint(1,101,10)
print("10 random integers between 1–100\n",random)
# Find shape, size, and dtype of an array
print(np.shape(arr2))
print(np.size(arr2))
print(arr2.dtype)



# Level 2: Indexing & Slicing
# Extract first row and last column from a matrix
matrix=np.random.randint(1,10,size=(3,3))
print("Original Matrix:\n",matrix)
print("After extract first row and last column from a matrix:")
print(matrix[0],matrix[-1])#indexing

# Reverse a 1D array

arr3=np.array([1,2,3,4])
rev=arr3[::-1]
print("Originally array\n",arr3)
print("reverse array\n",rev)
# Extract elements greater than 50
arr4=np.random.randint(1,20,size=(3,3))
print("Original array:\n",arr4)
filter_array=arr4[arr4>10]
print("Extract elements greater than 10",filter_array)
# Replace all negative values with 0
arr5=np.array([1,2,-3,4,-5,6])
print("Original array\n",arr5)
arr5[arr5<0]=0
print("Modified array\n",arr5)
# Get diagonal elements of a matrix
arr6=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array\n",arr6)
print("Digonal elements are\n",np.diag(arr6))

### Level 3: Reshape & Transform
# Convert a 1D array into 2D (3×4)
oned_arr=np.arange(1,13)
print("one_d array:\n",oned_arr)
twod_arr=oned_arr.reshape(3,4)
print("After Convert a 1D array into 2D (3×4)\n",twod_arr)
# Flatten a 2D array
print("Flatten a 2D array\n",twod_arr.flatten())

# Reshape a (2,3,4) array into (4,3,2)
threed_arr=np.random.randint(1,25,size=(2,3,4))
print("(2,3,4) array\n",threed_arr)
print("After reshape (4,3,2)\n",threed_arr.reshape(4,3,2))
# Stack two arrays vertically and horizontally
arr7=np.array([1,2,3])
arr8=np.array([4,5,6])
print("vertically\n",np.vstack((arr7,arr8)))
print("Horizontally\n",np.hstack((arr7,arr8)))
# Split an array into 3 equal parts
arr9=np.array([1,2,3,4,5,6,7,8,9,11,12,13])
print("Original array\n",arr9)
print("After split in 3 equal part\n",np.split(arr9,3))

# Level 4: Mathematical Operations
# Find mean, median, std of array
arr10=np.array([1,2,3,4,5,6,7,8,9,11,12,13])
print("Original array\n",arr10)
print("Mean:",arr10.mean())
print("Median:",np.median(arr10))
print("Std:",arr10.std())
# Normalize an array (0 to 1 range)
mean_=arr10.mean()
standard=arr10.std()
normalized_array=(arr10-mean_)/standard
print("Normalized_array\n",normalized_array)
# Find max and min along rows & columns
arr6=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array\n",arr6)
min_row=np.min(arr6,axis=1)
print("Row wise min value: ",min_row)
max_row=np.max(arr6,axis=1)
print("Row wise max value: ",max_row)
min_col=np.min(arr6,axis=0)
print("Coloumn wise min value: ",min_col)
max_col=np.max(arr6,axis=0)
print("Coloumn wise max value: ",max_col)

print("Max row is: ",np.max(arr6,axis=0))

print("Max coloumn is: ",np.max(arr6,axis=1))
# Compute dot product of two arrays
# Dot product=Multiply corresponding elements and then add them
arr7=np.array([1,2,3])
arr8=np.array([4,5,6])
print("Two arrays are:\n",arr7,arr8)
print("dot product of two arrays:",np.dot(arr7,arr8))
# Multiply two matrices
arr_7=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_8=np.array([[10,21,32],[24,52,63],[17,38,9]])
print("Two arrays are:\n",arr_7,"\n",arr_8)
print("After matrix multiplication\n",np.dot(arr_7,arr_8))

# Level 5: Broadcasting (Very Important)
# Add a scalar to a matrix
arr_7=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Add a scalar in matrix\n",arr_7+10)
# Subtract a row vector from each row
print("Original matrix\n",arr_7)
print("Subtract a row vector from each row\n",arr_7-arr_7[0])
# Subtract a column vector from each column
print("Original matrix\n",arr_7)
print("column vector: ",arr_7[:,0])
print("Subtract a column vector from each columns\n",arr_7-arr_7[:,[0]])
# Multiply a (3×1) with (1×4) → result shape?
mat1=np.random.randint(5,10,size=(3,1))
print("Matrix one\n",mat1)
mat2=np.random.randint(5,10,size=(1,4))
print("Matrix two\n",mat2)
result=np.dot(mat1,mat2)
print("Multiply two matrix\n",result)
print("result shape: ",result.shape)
# Fix broadcasting error in (3,2) + (3,)
array1=np.random.randint(1,10,size=(3,2))
array2=np.random.randint(1,10,size=(3,))
re=array2.reshape(3,1)
print("Array 1\n",array1)
print("Array 2\n",re)
addition=array1+re
print("Add two array using brodcasting\n",addition)
# Level 6: Missing Values
# Count number of NaN values
array3=np.array([[1,2,np.nan],[4,np.nan,6],[np.nan,np.nan,9]])
c=np.isnan(array3)
print("Array:\n",array3)
print("Number of nan value in array: ",c.sum())
# Replace NaN with mean
new_arr=np.nan_to_num(array3,nan=np.nanmean(array3))
print("Replace NaN with mean\n",new_arr)
# Remove NaN values
array_3=np.array([[1,2,np.nan],[4,np.nan,6],[np.nan,np.nan,9]])
rem=array_3[~np.isnan(array_3)]
print("After remove nan values\n",rem)
# Replace infinite values with 0
array4=np.array([[1,2,np.inf],[4,np.inf,6],[np.inf,np.inf,9]])
print(array4)
new_array=np.nan_to_num(array4,posinf=0)
print("Replace infinite values with 0\n",new_array)
# Use np.nan_to_num() on dataset
array5 = np.array([[1,2,np.nan],[4,np.nan,6],[np.nan,np.nan,9]])
newarr = np.nan_to_num(array5,nan=10)
print("Use np.nan_to_num() on dataset\n",newarr)
# Level 7: Advanced (Interview Level)
# Find unique elements and their counts
array6=np.array([[9,7,6],[1,2,1],[7,9,9]])
print("Original array\n",array6)
unique_value,count=np.unique(array6,return_counts=True)
print("Unique element\n",unique_value)
print("Their count\n",count)
# Sort array row-wise and column-wise
row_wise=np.sort(array6,axis=1)
print("Original array\n",array6)
print("After sorting row wise\n",row_wise)
column_wise=np.sort(array6,axis=0)
print("After sorting column wise\n",column_wise)
# Find index of max element
array7=np.array([[9,7,6],[1,2,18],[7,9,15]])
print("Original array\n",array7)
max_ele=array7.max()
print()
print("Maximum element index is:",max_ele)
# Create checkerboard pattern (0 & 1 matrix)
# Extract top 3 largest values

# Level 8: Real Interview Problems
# Create 6×6 matrix → extract submatrix (you did this 👍)
six_six_mat=np.random.randint(1,37,size=(6,6))
print("Original matrix\n",six_six_mat)
sub_mat=six_six_mat[3:,3:]
print("Sub matrix of the original matrix\n",sub_mat)
# Normalize each column separately
new_array1=np.array([[1,10],[2,20],[3,30]])
print(new_array1)
print("After normalize each column")
mean1=new_array1.mean(axis=0)
standard_de=new_array1.std(axis=0)
normalize=(new_array1-mean1)/standard_de
print(normalize)
print("2nd process")
normalize1=(new_array1-new_array1.min(axis=0))/(new_array1.max(axis=0)-new_array1.min(axis=0))
print(normalize1)

# Compute row-wise sum using axis
print("original Array\n",new_array1)
print("After row wise sum")
print(np.sum(new_array1,axis=1))
# Replace diagonal with specific values
array8=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original Array\n",array8)
np.fill_diagonal(array8,[10,11,12])
print("After replace diagonal with specific value\n",array8)
# Create sliding window (advanced)
windows=np.lib.stride_tricks.sliding_window_view(array8,(2,2))
print("Sliding Window view\n",windows)
