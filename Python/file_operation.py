#File Handeling is a crucial part of any  language.
# Python provide built-in function and method to read from and write to files,
# both txt and binary.

##write in a file
with open("My_info.txt","w") as f:
    f.write("Hello, my name is Jayanta Samanta. I am from West Medinipur.\n I completed my Bachelor of Computer Applications (BCA) degree from Panskura Banamali College in 2025 with a CGPA of 6.73.\n Currently, I am pursuing my Master of Computer Applications (MCA) at HIT, Haldia.\nThank you.")

#read a file

with open("My_info.txt","r") as f:
    # info=f.read()
    # print(info)
    for line in f:             #Read line by line
        print(line.strip())  #Strip() remove the new line charecter


##Write a file without overriding

with open("My_info.txt",'a') as f:
    f.write("\nAppend operation happen.")


##Writing a list of liens in a file

lines=["\nFirst line \nSecond line \nThird line"]
with open("My_info.txt",'a') as f:
    f.writelines(lines)

## Read a text file and count the number of lines,word,cherecters.

def count_text(file_path):
    with open(file_path,'r') as f:
        lines=f.readlines()
        count_lines=len(lines)
        count_word=sum(len(line.split())for line in lines)
        count_char=sum(len(line)for line in lines)
    return count_lines,count_word,count_char
file_path="My_info.txt"
lines,words,characters = count_text(file_path)
print(f"Lines:{lines} , Words:{words}, Characters:{characters}")

##Writing and the reading a file

with open("example.txt","w+") as f:
    f.write("Hello everyone")
    f.write("\n How are you.")
    #move the file cursor to the begining
    f.seek(0)
    content=f.read()
    print(content)
    f.seek(0) #move cursor agin begining
    print(f.read(5)) # read only first five char

    
