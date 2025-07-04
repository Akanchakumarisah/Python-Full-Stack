# Create a class Student with attributes name, roll, and marks. Use __init__() to initialize, and a method get_result() to return: 
#   "Pass" if marks >= 40, else "Fail" 
#   Create 3 objects and call the method.
class student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def get_result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"
# Create three student objects
student1 = student("Alice", "101", 85)
student2 = student("Bob", "102", 35)
student3 = student("Charlie", "103", 50)
# Call the get_result method for each student
print(f"{student1.name} (Roll: {student1.roll}) - Result: {student1.get_result()}")
print(f"{student2.name} (Roll: {student2.roll}) - Result: {student2.get_result()}")
print(f"{student3.name} (Roll: {student3.roll}) - Result: {student3.get_result()}")