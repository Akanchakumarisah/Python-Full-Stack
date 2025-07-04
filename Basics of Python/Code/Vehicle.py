from abc import ABC, abstractmethod 
class Vehicle:
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")
my_car = Car()
my_bike = Bike()
my_car.start_engine()
my_bike.start_engine()
