#polymorphism
#parent class Animal
class Animal:
    def sound(self):
        return "Animal makes a sound"

#derive class or child class Dog
class Dog(Animal):
    def sound(self):
       return "Dog barks"

#derive class or child class Cat
class Cat(Animal):
    def sound(self):
        return "Cat meows"

#derive class or child class Cow
class Cow(Animal):
    def sound(self):
        return "Cow moos"

# Function to demonstrate polymorphism to treat all different object derive from the same class.
def sound_of_animal(animal_obj):

    print(animal_obj.sound())# calling the method of the object
    print(animal_obj.sound)#reference to the method give location of the method in memory
# Create instances of each animal
dog1 = Dog()
cat1 = Cat()
cow1 = Cow()

# Call the function with different animal objects or method callind
sound_of_animal(dog1)  # Dog barks
sound_of_animal(cat1)  # Cat meows
sound_of_animal(cow1)  # Cow moos

