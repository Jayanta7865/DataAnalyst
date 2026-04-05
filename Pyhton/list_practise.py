# # Module 3: Data Structures Assignments
# ## Lesson 3.1: Lists
# ### Assignment 1: Creating and Accessing Lists

# Create a list of the first 20 positive integers. Print the list.
numbers=[]
for i in range(1,21):
    numbers.append(i)

print("Print the first positive 20 element\n",numbers)

# ### Assignment 2: Accessing List Elements

# Print the first, middle, and last elements of the list created in Assignment 1.
first,*middle,last=numbers
print("Print the first elements: ",first)
print("Print the middle elements: ",middle)
print("Print the last elements:",last)

# ### Assignment 3: List Slicing

# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
print("Print the first five elements\n",numbers[:5])
print("Print the last five elements\n",numbers[15:20])
print("Print 5-15 index elements\n",numbers[4:15])

# ### Assignment 4: List Comprehensions

# Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
num=[1,2,3,4,5,6,7,8,9,10]
squaree_num=[x**2 for x in num]
print("Square of the list item",squaree_num)

# ### Assignment 5: Filtering Lists

# Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.

even_num = [x for x in numbers if x % 2 == 0]
print("Find even number using list comprehension",even_num)
print("Even number between 1-20: ",numbers[1:20:2])
# ### Assignment 6: List Methods

# Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.
ran_num=[2,5,7,8,1,2,3,9,10,3]
print("The random list is:",ran_num)
ran_num.sort()
print("List number print in accending order:",ran_num)
ran_num.reverse()
print("List number print in descending order:",ran_num)
unique_num=[]
for num in ran_num:
    if num not in unique_num:
        unique_num.append(num)
print("Delete duplicate value in list:",unique_num)
# ### Assignment 7: Nested Lists

# Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
print("3*3 matrix")
for sub_list in nested_list:
    for num in sub_list:
        print(num,end=" ")
    print(" ")
print("Second row of matrix:",nested_list[1])
print("Print 2nd row 3rd column element:",nested_list[1][2])

# ### Assignment 8: List of Dictionaries

# Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.
students=[{'Name':'Jayanta','Score': 60},
         {'Name':'Sumana','Score': 55},
         {'Name':'Ram','Score': 40},
         {'Name':'Rahul','Score': 98},]
# def get_score(student): #first process
#     return student['Score']
# sorted_std=sorted(students,key=get_score,reverse=True)
sorted_std=sorted(students,key=lambda x:x['Score'],reverse=True) #2nd process
print("Sorted students by score in descending order:")
for student in sorted_std:
    print(student)




# ### Assignment 9: Matrix Transposition

# Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.
def transposition_matrix(matrix):
     transposed=[[matrix[j][i] for j in range (len(matrix))] for i in range (len(matrix[0]))]
     return transposed
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
transpose=transposition_matrix(matrix)
print("Original matrix")
for row in matrix:
    print(row)
print("Transposed matrix:")
for row in transpose:
    print(row)

# ### Assignment 10: Flattening a Nested List

# Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.
lst=[[1,2,3],[4,5,6]]
flattens_list=[]
for sub_lst in lst:
    for num in sub_lst:
        flattens_list.append(num)

print("Original list",lst)
print("flattened lists",flattens_list)
# flat=[item for sub_list in lst for item in sub_list]
# print(flat)
# ### Assignment 11: List Manipulation

# Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified list.
num=[1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {num}")
del num[6]
del num[4]
del num[2]
num.insert(5,99)
print(f"Modified list: {num}")

# ### Assignment 12: List Zipping

# Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.
# zip function is in built function that use for combine item index wise.
lst1=[1,3,4,6,5]
lst2=['a','e','i','jayanra','c']
pair=list(zip(lst1,lst2))
print(pair)

# ### Assignment 13: List Reversal

# Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.
def rev_lst(lst):
     revese_lst=lst[::-1]
     print("Original list",lst)
     print("Reversed list",revese_lst)
     
     
rev_lst([3,4,5,6,7])

# ### Assignment 14: List Rotation

# Write a function that rotates a list by n positions. Print the original and rotated lists.


# ### Assignment 15: List Intersection

# Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list.

def new_lst(lst1,lst2):
     intersected_list=[]
     print(f"List 1: {lst1}")
     print(f"List 2: {lst2}")
     
     for i in lst1:
          if i in lst2 and i not in intersected_list:
                    intersected_list.append(i)
     return intersected_list
result=new_lst([2,3,4,5,6],[2,90,34,5,3,2])
print(f"Intersection: {result}")
