#single class inheritance
class Animal:
    def __init__(self,name):
        self.name = name
        print("name of animal is", self.name)

#methods
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def __init__(self,name,color,breed):
        super().__init__(name)
        self.color=color
        self.breed=breed
        #behaviours of dog
    def make_sound(self):
        print("Dog barks")

#creating object of Dog class
dog1 = Dog("Tommy","Brown","Labrador")

#calling methods
dog1.speak()

