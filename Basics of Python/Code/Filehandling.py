#file handling
#Opeing a file
#f=open('file1.txt',r)
#Reding a file
#f.read() #reads the entire file
#f.readline() #reads a single line
#f.readlines() #reads all lines and returns a list
#Writing to a file
#f=open('file1.txt','w') #opens the file in write mode, overw
#f.write('Hello World') #writes to the file
#Appending to a file
#f=open('file1.txt','a') #opens the file in append mode
#f.write('Hello World') #appends to the file
#Closing a file
#f.close() #closes the file 
# File handling in Python
# Opening a file in read mode
with open('file1.txt', 'r') as f:
    # Reading the entire file
    content = f.read()
    print("File Content:")
    print(content)
    # Opening a file in write mode
    with open('file2.txt', 'w') as f:
        # Writing to the file
        f.write("Hello World\n")
        f.write("This is a new file.\n")
        print("Data written to file2.txt")
    # Appending to a file
    with open('file2.txt', 'a') as f:
        f.write("Appending this line to file2.txt\n")
        print("Data appended to file2.txt")
    # Reading the file again to see the changes
    with open('file2.txt', 'r') as f:
        updated_content = f.read()
        print("Updated file2.txt Content:")
        print(updated_content)  
        # Closing the file is handled automatically by the 'with' statement
        # File handling with error handling
        try:
            with open('non_existent_file.txt', 'r') as f:
                content = f.read()
          except FileNotFoundError:
            print("Error: The file does not exist.")
        except IOError: 
            print("Error: An I/O error occurred.")
            # File handling with error handling
            try:
                with open('file2.txt', 'r') as f:
                    content = f.read()
                    print("File Content:")
                    print(content)
              except FileNotFoundError:
                print("Error: The file does not exist.")
            except IOError:
                print("Error: An I/O error occurred.")
                #closing the file is handled automatically by the 'with' statement
                # File handling with context manager
                
        