#Multiple except block
try:
    file1 = open("nonexistent.txt", "r")
    data = file1.read()
    print(data)
except FileNotFoundError as e:
    print("FileNotFoundError: The file does not exist.")
except IOError as e:
    print("IOError: An error occurred while reading the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}") 
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")