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

