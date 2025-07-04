try:
    file1=open("nonexistent.txt","r")
    data=file1.read()
    print(data)
except FileNotFoundError as e:
    print("file1 doestnot exist")
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")
