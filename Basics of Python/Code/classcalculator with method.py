#create a class calculator with methods for addition, subtraction, multiplication, and division
class calculator:
    def add(self,num1,num2):
        return num1+num2
    def sub(num1,num2):
        return num1 - num2
    def mul(num1,num2):
        return num1 * num2
    def div(num1,num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
        
num1 = float(input("Enter first number: "))
num2= float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
calc = calculator()
if operator == '+':
        print("Result:", calc.add(num1, num2))
elif operator == '-':
        print("Result:", calc.sub(num1, num2))
elif operator == '*':
        print("Result:", calc.mul(num1, num2))
elif operator == '/':
        print("Result:", calc.div(num1, num2))
else:
        print("Invalid operator")