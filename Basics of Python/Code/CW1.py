#1. Accept 3 lines from user and save to user_input.txt
#2. Read and display content of user_input.txt
#3. Append data in the file to log.txt
f= open("user_input.txt", "w")
for i in range(3):
    line = input(f"Enter line {i+1}: ")
    f.write(line + "\n")
#2. Read and display content of user_input.txt
f.close()
with open("user_input.txt", "r") as f:
    content = f.read()
    print("Content of user_input.txt:")
    print(content)
    #3. Append data in the file to log.txt
    with open("log.txt", "a") as log_file:
        log_file.write(content)
        print("Content appended to log.txt")
        # Closing the file is handled automatically by the 'with' statement
        f.close()
        

