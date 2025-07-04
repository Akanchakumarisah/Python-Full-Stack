#Opening a file in read mode
f=open('C:/Users/HP/OneDrive/Desktop/Pythonfile1/Basics of python/file1.txt','r')
read_txt=f.readlines()#this will return the file text in the form of
print(read_txt,"\n")
f.close()

#return the text written in the file by using for loop
for line in read_txt:
    print(line.strip())  # strip() removes leading/trailing whitespace including newlines


#readlines() reads all lines and returns a list


#Opeing a file in write mode
f=open('C:/Users/HP/OneDrive/Desktop/Pythonfile1/Basics of python/file2.txt','w')
f.write("Hello World\n")
f.write("This is a new file.\n")
print("Data written to file2.txt\n")
with open('C:/Users/HP/OneDrive/Desktop/Pythonfile1/Basics of python/file2.txt','a') as f:
    f.write("Appending this line to file2.txt\n")
    print("Data appended to file2.txt\n")
f.close()
#read operation by using with open() as f:
with open('C:/Users/HP/OneDrive/Desktop/Pythonfile1/Basics of python/file2.txt','r') as f:
    updated_content = f.read()
    print("Updated file2.txt Content:")
    print(updated_content)
    #to check if the file is exexting in a system or not
    import os
    if os.path.exists('C:/Users/HP/OneDrive/Desktop/Pythonfile1/Basics of python/file2.txt'):
        print("File exists.")
    else:
        print("File does not exist.")
#removing a file    
import os
# Check if the file exists before attempting to remove it
file_path = 'C:/Users/HP/OneDrive/Desktop/Pythonfile1/Basics of python/file2.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been removed.")
else:
    print(f"{file_path} does not exist, so it cannot be removed.")

#file handling with exception handling
try:
    with open('C:/Users/HP/OneDrive/Desktop/Pythonfile1/Basics of python/non_existent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
        print("file does not found)")
#to store user data in a file
# Opening a file in append mode
"""with open("User.txt","a") as f:
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    f.write(f"Name: {name}, Age: {age}\n")

    #read the file and print the values
with open('User.txt', 'r') as log_file:
    for product in log_file:
        print(product)"""

from datetime import datetime
with open("log.txt", "a") as f:
    f.write(f"Log entry at {datetime.now()}\n")



   
   
    #f.append(f"Name: {name}, Age: {age}\n")

#opeing a file in append mode
#we can also open file by using with open() as f:
"""f=open('C:/Users/HP/OneDrive/Desktop/Pythonfile1/Basics of python/file2.txt','a')
f.write("Appending this line to file2.txt\n")
print("Data appended to file2.txt\n")
f.close()"""
#Create
#text mode
#binary
#Writting logs or report



