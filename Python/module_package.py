# import math
# print(math.lcm(24,2))
# print(math.sqrt(100))# square root
# print(math.factorial(4))

# #import perticualar function
# from math import sqrt,pi,factorial
# print(sqrt(100))
# print(pi)
# print(factorial(4))

# # using * we can import everything from a module module 

# from math import *
# angle =acos(0)  
# print(degrees(angle))
 

from My_package.math import *

print(mul(23,2))
print(sub(23,26))
print(addition(23,2))
try:
  print(addition(23,2))
  print(div(2,0))
except ZeroDivisionError as e:
    print(e)
print(mod(23,2))

print(greet())

#standard library

import array
print(array.array('i',[1,2,3,4])) # i is the typecode. it take only integer value
print(array.array('f',[1.2,2.5,3.0,4.0])) # it take only float value
print(array.array('d',[1,2,3,4]))   # it take only doubble value
print(array.array('u','jayanta'))    # it take only string


import random
gess=int(input("Enter a number between 1-6: "))
num=random.randint(1,6)
if gess==num:
   print("Your number is match with actual number.")
else:
   print("Sorry!Batter luck next time")
   print("Actual number is",num)

choice=random.choices(["a",'e','i','o','u'],k=2)
print(choice)
print(random.gauss())
print(random.randrange(1,10,2))


import os
print(os.getcwd())
os.makedirs("Jayanta_dr") # make a new folder

#High level operation on fiels or collection of fiels

import shutil
shutil.copyfile("demo.txt","My_info.txt")

print(os.path.exists("demo.txt"))