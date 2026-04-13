#Exception handling is used to handle runtime errors so your program doesn’t
#  crash and runs smoothly
#Types of Exceptions (Common):
# ZeroDivisionError → division by zero
# ValueError → wrong data type
# FileNotFoundError → file not found
# IndexError → list index out of range

# try → risky code
# except → handle error
# else → runs if no error
# finally → always runs
# raise → create your own error

try:
    result=1/0
    print(result)
except ZeroDivisionError as e:
    print(e)

try:
    lst=[1,2,3,4]
    print(lst[5])

except IndexError as e:
    print(e)

try:
    num=int(input("Enter demoninator: "))
    result=10/num
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("program terminated")

##File hendaling and Exception handeling

try:
    file=open("example.txt","r")
    content=file.read()
    print(content)
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print("File closed")
    print("Progrem Ended")


import os
try:
    os.mkdir("Jayanta")
    print("creat successfuly")
except FileExistsError as e:
    print(e)



