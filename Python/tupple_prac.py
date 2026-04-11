# # Module 3: Data Structures Assignments
# ## Lesson 3.2: Tuples
# ### Assignment 1: Creating and Accessing Tuples

# Create a tuple with the first 10 positive integers. Print the tuple.

num=tuple(range(1,11))
print(num)

# ### Assignment 2: Accessing Tuple Elements

# Print the first, middle, and last elements of the tuple created in Assignment 1.
print("First element",num[0])
print("Middle element",num[len(num)//2])
print("Last element",num[-1])
# ### Assignment 3: Tuple Slicing

# Print the first three elements, the last three elements, and the elements from index 2 to 5 of the tuple created in Assignment 1.
print("First three element",num[0:3])
print("Last three element",num[7:10])
print("2-5 element",num[1:5])
# ### Assignment 4: Nested Tuples

# Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
matrix=((1,2,3),(4,5,6),(7,8,9))

for i in matrix:
    print(i)

print("the element at the second row and third column:",matrix[1][2])
print(matrix)

# ### Assignment 5: Tuple Concatenation

# Concatenate two tuples: (1, 2, 3) and (4, 5, 6). Print the resulting tuple.
tup1=(1,2,3)
tup2=(4,5,6)
con=tup1+tup2
print(con)


# ### Assignment 6: Tuple Methods

# Create a tuple with duplicate elements and count the occurrences of an element. Find the index of the first occurrence of an element in the tuple.
num=(1,2,3,3,3,4,5,1,6,4)
print(num.count(3))
print(num.index(3))

# ### Assignment 7: Unpacking Tuples

# Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.
a,b,c,d,e=(2,4,5,6,7)
print(a)
print(b)
print(c)
print(d)
print(e)

# ### Assignment 8: Tuple Conversion

# Convert a list of the first 5 positive integers to a tuple. Print the tuple.
lst=[1,2,3,4,5]
tup=tuple(lst)
print(tup)

# ### Assignment 9: Tuple of Tuples

# Create a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.
tups=(("ram","sam","jodu"),
      (2,3,4),
      (2.5,"jayanta,",3))
for tuples in tups:
    print(tuples)

# ### Assignment 10: Tuple and List

# Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.
tup=(1,2,3,4,5)
lst=list(tup)
lst.append(6)
tup2=tuple(lst)
print(tup2)

# ### Assignment 11: Tuple and String

# Create a tuple with the characters of a string. Join the tuple elements into a single string. Print the string.
string="JAYANTA"
tup=tuple(string)
joind_tup=''.join(tup)
print(joind_tup)
# ### Assignment 12: Tuple and Dictionary

# Create a dictionary with tuple keys and integer values. Print the dictionary.
tpl_dict = {
    (1, 2): 3,
    (4, 5): 6,
    (7, 8): 9
}
print(tpl_dict)

# ### Assignment 13: Nested Tuple Iteration

# Create a nested tuple and iterate over the elements, printing each element.
nested_tup=((1,2,3),
            (4,5,6),
            (7,8,9))
for sub_tup in nested_tup:
    for num in sub_tup:
        print(num)

# ### Assignment 14: Tuple and Set

# Create a tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.
num=(1,3,4,1,5,2,4,9)
set_tup=set(num)                                                                             
print(set_tup)

# ### Assignment 15: Tuple Functions

# Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.
def min_tup(tup):
    return min(tup)
def max_tup(tup):
    return max(tup)
def sum_tup(tup):
    return sum(tup)
sample_tup=(5,7,9,10,3,45)
print(f"Min value in tupple {min_tup(sample_tup)}")
print(f"Max value in tupple {max_tup(sample_tup)}")
print(f"Sum of all tupple items {sum_tup(sample_tup)}")

