from Python.My_package.math import *

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
