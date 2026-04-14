##insert element
#syntax=np.insert(array,index_no.,value,axis=none) for 1d array
##syntax=np.insert(array,index_no.,value,axis=0) for 2d array if we insert row wise other then axis=1

import numpy as np
arr=np.array([1,2,3,4,5,6])
new_arr=np.insert(arr,3,10,axis=None)
print(new_arr)

##for 2d
arr_2d=np.array([
    [1,2],[3,4]
])

new_2d=np.insert(arr_2d,2,[5,6],axis=0)
print(new_2d)
new_2d=np.insert(arr_2d,2,[10,11],axis=1)
print(new_2d)

#for 3d
arr_3d=np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print(arr_3d)
new_3d=np.insert(arr_3d,2,[5,6],axis=0)
print(new_3d)

##append

arr1=np.array([1,2,3,4,5,6])
new_arr1=np.append(arr1,[7,8,9,10])
print(new_arr1)

arr_2d1=np.array([
    [1,2],[3,4]])
new_2d1=np.append(arr_2d1,[[5,6]],axis=0)
print(new_2d1)

##concatinate

arr_1=np.array([1,2,3])
arr_2=np.array([4,5,6])
new_array=np.concatenate((arr_1,arr_2))
print(new_array)

##remove element in an array
##syntax=np.delete(array,index,axis=none/0/1)

after_del=np.delete(new_array,4,axis=None)
print(after_del)

#for 2d

after_del2d=np.delete(new_2d1,2,axis=0)
print(new_2d1)
print(after_del2d)

##Stacking:In NumPy,stacking is used to join arrays row-wise, 
# column-wise, or depth-wise.
# Vertical Stacking (vstack) → Row-wise
array1=np.array([1,2,3])
array2=np.array([4,5,6])
print(np.vstack((array1,array2)))

# Horizontal Stacking (hstack) → Column-wise
print(np.hstack((array1,array2)))


# Spliting:
# Splitting means dividing a large array into multiple 
# smaller sub-arrays.
# In NumPy, we use functions like:
# split()=Split into equal parts
##syntex=np.split(array,no.sub split)
array_1=np.array([1,2,3,4,5,6])
new=np.split(array_1,3)
print(new)

# hsplit()=Horizontal Split (hsplit) → Column-wise for 2d and md
##syntex:- np.hsplit(array,no of sub split)
td=np.array([[1,2,3,12],[4,5,6,11],[7,8,9,10],[23,45,56,34]])
new1=np.hsplit(td,2)
print(new1)
# vsplit()=Vertical Split (vsplit) → Row-wise
##syntex: np.vsplit(array,no of sub split)
new2=np.vsplit(td,2)
print(new2)
# dsplit()=Depth Split (dsplit) → 3D
##syntex:-np.dsplit(array,no of sub split)
arr12 = np.array([[[1,2,3,4]],[[5,6,7,8]]])
print(arr12.shape)
print(np.dsplit(arr12, 2))

