# #Lambda function:-
# A lambda function in Python is a small, anonymous (unnamed) function defined using the lambda keyword.
# It is typically used for short, one-line operations where defining a full function using def is unnecessary.

# #syntax= lambda argument:expression.

addtion=lambda a,b,c:a+b+c
'''This the examle of lambda function'''
print(addtion(3,4,5))

# # #odd and even using lambda

odd_even=lambda n:"Even" if n%2==0 else "odd"
print(odd_even(7))
print((lambda n:"Even" if n%2==0 else "odd")(12))
# #  factorial use lamda 
fact= lambda n: 1 if n==0 or n==1 else n*fact(n-1)
print(fact(0))

# ## map function:-

# #The map() function is a built-in function in Python used to apply a 
# # function to each element of an iterable (like list, tuple, etc.)
# #  and return a new iterable (map object).
# ## syntax= map(function,itterable)

def square(n):
    return n**2
lst=[2,3,4]
print(list(map(square,lst)))

# ###  lambda function with map

cube=list(map(lambda x:x**3,lst))
print(cube)

#odd even use map
def odd_even(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
tup=(2,3,4,5,6,7,8,9)
check=list(map(odd_even,tup))

## using lambda
my_tup=(2,4,6,8,1)
odd_even=list(map(lambda num:"even" if num%2==0 else "odd",my_tup))
print(odd_even)


## convert string int into int use map

string_int=['1','2','3','4','5']
number=list(map(int,string_int))
print(number)

# capital first latter
lst=["apple","banana","cherry","mango"]
cap=list(map(str.capitalize,lst))
print(cap)

## count  any alphabet in list
counts = list(map(lambda x: x.count('a'), lst))
print(counts)

#####  Filter function
#The filter() function is a built-in function used to select elements from an iterable
#  based on a condition.
# syntax- filter(function,itterable)

def check(num):
    return num%2==0
tup=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(list(filter(check,tup)))

## filter with lambda

print(list(filter(lambda num:num%2==0,(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))))

fruits=["apple","banan","cherry","mango","guava","watermillon"]
print(list(filter(lambda x: len(x)<=5,fruits)))

##people who aligible for vote

people_age=[21,34,56,54,12,7,98,18,37,11,19]
print(list(filter(lambda x:x>=18,people_age)))







