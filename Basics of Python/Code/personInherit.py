class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display_info(self):
        print(f"Roll Number: {self.roll_number} Name: {self.name} Age: {self.age}")
student1 = Student("Alice", 20, "S123")
student1.display_info()