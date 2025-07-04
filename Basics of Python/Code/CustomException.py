class AgeToolError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age must be a positive integer.")#why supper().__init__ is used here?
age=int(input("Enter your age: "))
if age<18:
    raise AgeToolError(age)
else:
    print("You are eligible to use this tool.")
try:
    raise AgeToolError(age)
except AgeToolError as e:
    print("custom exception:", e)
finally:
    print("Thank you for using the Age Tool.")



