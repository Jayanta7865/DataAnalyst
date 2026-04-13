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

#data serialization
import json
data={"name":"jayanta","age":20,"emial":"xyz@gmail.com"}
json_str=json.dumps(data)
print(json_str)
print(type(json_str))

json_dic=json.loads(json_str)
print(json_dic)
print(type(json_dic))


##datetime

from datetime import datetime,timedelta,date
now=datetime.now()  #print date + time today
print(now)

yesterday=now-timedelta(days=1)
print(yesterday)  # print date + time yesterday

today=date.today()
print(now.strftime("%d-%m-%y"))  #print only date

time=datetime.now().time()
print(now.strftime("%H:%M:%S")) #print only time

##csv
import csv

with open ("demo.csv",mode="w",newline="") as f:
   writer=csv.writer(f)
   writer.writerow(["massege"])
   writer.writerow(["hello my name is jayanta."])
with open("demo.csv",mode='r') as f:
   read=csv.reader(f)
   for row in read:
      print(row)