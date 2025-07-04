# Simple Calculator
"""num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /,%,+=,-=,*=,&,|,<,>): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
elif operator == '%':
    print("Result:", num1 % num2)
elif operator == '+=':
    num1 += num2
    print("Result:", num1)
elif operator == '-=':
    num1 -= num2
    print("Result:", num1)
elif operator == '*=':
    num1 *= num2
    print("Result:", num1)
elif operator == '&':
    print("Result:", num1 & num2)
elif operator == '|':
    print("Result:", num1 | num2)
elif operator == '<':
    print("Result:", num1 < num2)       
elif operator == '>':
    print("Result:", num1 > num2)
elif operator == '==':
    print("Result:", num1 == num2)

elif operator == '!=':
    print("Result:", num1 != num2)
else:
    print("Invalid operator")"""

# User Login System
"""user_name=str(input("Enter your username: "))
password=str(input("Enter your password: "))
if user_name == "Akancha" and password == "1234":
    print("Login successful")
else:
    print("Login failed")"""


# Grade Calculator
"""grade = int(input("Enter your grade: "))

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("E")"""

    #loop in python
"""for i in range(2,10,2):
    print(i)
    if i>3:
        break
else:
    print("Loop finished")"""
"""for i in range(5):
    print(i)
    while i > 3:
       break
    else:
        print("Loop finished")"""
#list
"""fruits=['apple', 'banana', 'cherry',]
numbers=[1, 2, 3, 4, 5]
print(fruits)
print(numbers)
print(fruits[0])
print(numbers[0])
#appending to list
fruits.append('orange')
print(fruits)
numbers.clear()
print(numbers)
print(fruits.copy())
print(fruits.count('apple'))
print(fruits.index('banana'))
fruits.insert(1, 'kiwi')
print(fruits)
#extending list
fruits.extend(['mango', 'grape'])
print(fruits)
fruits.remove('kiwi')
print(fruits)
#reversing list
fruits.reverse()
print(fruits)
#sorting list
fruits.sort()
#fruits = sorted(fruits)
print(fruits) 
fruits.pop()  # Removes the last item
print(fruits)  """

# create a list which contain threṇe cities
# cities = ['New York', 'Los Angeles', 'Chicago']
# cities.append('San Francisco') # Adding a new city
# cities.insert(2,'Houston')  # Adding a new city at index 2
# cities.remove('Los Angeles')# Removing a city
# cities.pop(0)
# print(cities)  # Displaying the updated list of cities
# 
#tuple
# Create a tuple with three cities
# cities_tuple = ('New York', 'Los Angeles', 'Chicago')
# print(cities_tuple)
#Accessing elements in a tuple
# print(cities_tuple[0])  # Output: New York
#tupple unpacking
#  cities_tuple = ('New York', 'Los Angeles', 'Chicago')
# city1, city2, city3) = cities_tuple
# print(city1)  # Output: New York


#Dictionary
stud = {"Name":"Akancha", "Degree":"Btech"}
print(stud)
print(stud["Name"])
print(stud["Degree"])

#common dictionary method

"""#clear in dictionary
stud.clear()  # Removes all items from the dictionary
print(stud)  # Output: {}
#copy in dictionary
stud = {"Name": "Akancha", "Degree": "Btech"}
stud_copy = stud.copy()  # Creates a shallow copy of the dictionary
print(stud_copy)  # Output: {'Name': 'Akancha', 'Degree': 'Btech'}      
formkeys = stud.keys()  # Returns a view object containing the keys of the dictionary
print(formkeys)  # Output: dict_keys(['Name', 'Degree'])
#values in dictionary
formvalues = stud.values()  # Returns a view object containing the values of the dictionary
print(formvalues)  # Output: dict_values(['Akancha', 'Btech'])
#items in dictionary
formitems = stud.items()  # Returns a view object containing the key-value pairs of the dictionary
print(formitems)  # Output: dict_items([('Name', 'Akancha'), ('Degree', 'Btech')])
#pop in dictionary
stud = {"Name": "Akancha", "Degree": "Btech"}
removed_value = stud.pop("Degree")  # Removes the key "Degree" and returns its value
print(removed_value)  # Output: Btech
print(stud)  # Output: {'Name': 'Akancha'}
#popitem in dictionary
stud = {"Name": "Akancha", "Degree": "Btech"}
removed_item = stud.popitem()  # Removes and returns the last inserted key-value pair
print(removed_item)  # Output: ('Degree', 'Btech')
print(stud)  # Output: {'Name': 'Akancha'}
#update in dictionary
stud = {"Name": "Akancha", "Degree": "Btech"}
stud.update({"Age": 20})  # Adds a new key-value pair to the dictionary
print(stud)  # Output: {'Name': 'Akancha', 'Degree': 'Btech', 'Age': 20}"""

#create a dictionary with 5 key-value pairs
"""student = {
    "Name": "Akancha",
    "Degree": "Btech",
    "Age": 20,
    "University": "XYZ University",
    "Year": 2023
}
print(student)
print(student.get("Name"))  
print(student.get("Gender", "Not Specified"))  # Output: Not Specified"""
#set in python
"""create_set = {1, 2, 3, 4, 5}
# Displaying the set
print(create_set)  # Output: {1, 2, 3, 4, 5}
# Adding a new number to the set        
numbers_set = {1, 2, 3}
# Adding a new number to the set
numbers_set.add(4)
print(numbers_set)  # Output: {1, 2, 3, 4}
#length of set
print(len(numbers_set))  # Output: 4
#in operator in set
print(2 in numbers_set)  # Output: True
#not in operator in set
print(5 not in numbers_set)  # Output: True
#t.issubset() method in set
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(set_a.issubset(set_b))  # Output: True
#t.issuperset() method in set
set_c = {1, 2, 3, 4, 5}
set_d = {1, 2, 3}
print(set_c.issuperset(set_d))  # Output: True
#t.union() method in set
set_e = {1, 2, 3}
set_f = {4, 5, 6}
set_union = set_e.union(set_f)  # Combines two sets
print(set_union)  # Output: {1, 2, 3, 4, 5, 6}
#t.intersection() method in set
set_g = {1, 2, 3}
set_h = {2, 3, 4}           
set_intersection = set_g.intersection(set_h)  # Finds common elements
print(set_intersection)  # Output: {2, 3}
#t.difference() method in set
set_i = {1, 2, 3}
set_j = {2, 3, 4}
set_difference = set_i.difference(set_j)  # Finds elements in set_i not in set_j
print(set_difference)  # Output: {1}
#t.symmetric_difference() method in set
set_k = {1, 2, 3}
set_l = {2, 3, 4}
set_symmetric_difference = set_k.symmetric_difference(set_l)  # Finds elements in either set but not both
print(set_symmetric_difference)  # Output: {1, 4}"""

"""#Create a set
my_set = {1, 2, 3, 4, 5}
print(my_set)
#add another unique element in a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
#try to add the same element which is already present"""



