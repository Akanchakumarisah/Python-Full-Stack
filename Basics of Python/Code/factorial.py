def factorial(n):
    """Calculate the factorial of a number n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
num = int(input("Enter a non-negative integer: "))
result = factorial(num)
print("The factorial of", num, "is:", result)