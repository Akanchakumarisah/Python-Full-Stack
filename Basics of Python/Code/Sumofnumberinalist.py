#Write a function sum_numbers(lst) that returns the sum of all numbers in a list.
def sum_number(lst):
    totalsum=0
    for number in lst:
        totalsum=totalsum+number
    return totalsum
lst = [1, 2, 3, 4, 5]
result = sum_number(lst)
print("The sum of the numbers in the list is:", result)