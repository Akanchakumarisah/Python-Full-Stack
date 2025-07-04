#Defining a function to greet the user
"""def greet_user(name):
    print(f"Hello, {name}! Welcome to the program.")

greet_user("Akancha")"""

def max_number(n1,n2):
    if(n1>n2):
        return n1
    else:
        return n2
    
n1=int(input("enter the n1: "))
n2=int(input("enter the n2: "))
result=max_number(n1,n2)
print("the maximum number is:", result)