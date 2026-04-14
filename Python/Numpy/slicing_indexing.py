##Access array element with index

## syntex:- veriable_name[index_no.] for 1d array
##syntex:- veriable_name[row,column] for 2d array
##syntex:- veriable_name[block,row,column] for 3d array
import numpy as np
arr=np.array([23,34,56,87]) #index start from 0
print(arr[2])
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2.ndim)
print(arr2[0,1]) #print 2
arr3=np.array([
    [[1,2],[4,5]],
    [[11,22],[44,55]],
])
print(arr3)
print(arr3[0,1,1])

##slicing
# “Slicing is a method of extracting a subset of elements from a
#  sequence using index ranges. It follows the syntax [start:end:step],
#  where the end index is excluded.”

arr4=np.array([10,20,30,40,50,60,70,80,90,100])
print(arr4[1:6]) #return index 1 - 5 value
print(arr4[:7]) #return index 0 - 6 value
print(arr4[::2]) # return every second element
print(arr4[::-1]) #reverse array
print(arr4[-5:-1]) # return len(array)-5 to len(array)-1 (60-90)

##Fancy indexing
##Fancy Indexing is a technique used to access multiple elements of 
# an array using lists or arrays of indices instead of simple slicing.

#syntax=array[[rows],[columns]] for 2d 
#syntax= array[[bolks],[rows],[column]] for 3d
arr5=np.array([10,20,30,40,50,60,70,80,90,100])
print(arr5[[0, 4, 9]])

md_d=np.array([
   [ [1,2,3],
    [4,5,6],
    [7,8,9]],

    [ [11,22,33],
    [44,55,66],
    [77,88,99]]

])

print(md_d.shape)
print(md_d)

print(md_d[[0,0],[0,1],[0,2]]) #3d array
two_d=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
print(two_d.shape)
print(two_d[[0,2],[1,2]])#2d array


##slicing with 2d and 3d array
#syntax=array[row,column] for 2d array
t_d=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
print(t_d[0:3,0:2])

##syntex:- array[block,row,column] for 3d array

m_d=np.array([
   [ [1,2,3],
    [4,5,6],
    [7,8,9]],

    [ [11,22,33],
    [44,55,66],
    [77,88,99]]
])

print(m_d[0:2,1:3,1:3])

##Boolean maskiing/filtaring
##Boolean Masking is a method to filter elements of an array
#  using True/False conditions.
##syntax=array[condition]
arr_4=np.array([10,20,30,40,50,60,70,80,90,100])
print(arr_4[arr_4>50])
