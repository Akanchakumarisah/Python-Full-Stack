# Encapsulation in Python OOP
class Students:
    def __init__(self, name, age, marks):
        self.name = name          # public attribute
        self._age = age           # protected attribute (by convention)
        self.__marks = marks      # private attribute

    # public method to display student info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Marks: {self.__marks}")  # corrected attribute

    # getter for private attribute
    def get_marks(self):
        return self.__marks

    # setter for private attribute
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100.")

# Creating object of Students class
student1 = Students("John", 21, 85)

# Accessing data using public method
student1.display_info()

# Accessing and modifying private data using getter/setter
print("Current Marks:", student1.get_marks())

student1.set_marks(95)  # Valid update
print("Updated Marks:", student1.get_marks())

student1.set_marks(150)  # Invalid update
try:
    print("Attempting to access private attribute directly:", student1.__marks)  # This will raise an AttributeError
except AttributeError:
    print("AttributeError: 'Students' object has no attribute '__marks'")
