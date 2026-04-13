import os
cwd=os.getcwd() # return current working dir
print(f"Current working directory is {cwd}")

# ##creat new dir

os.mkdir("Jayanta")
print("Directary Jayanta Creat successfully!")

# ##listing file and directories

list=os.listdir('.') #return all file and directry in cwd
print(list)

# #check the path is exit or not
path="example1.txt"
if os.path.exists(path):
    print(f"The path {path} is already exit.")
else:
    print(f"The path {path} can't exit.creat first.")
    os.mkdir(path)
    print("path is created")

##Getting the absolute path

path="example1.txt"
absulute_path=os.path.abspath(path)
print(absulute_path)


#creat folder inside a folder

import os
os.mkdir("Python/Numpy")  ## parent folder/child folder
