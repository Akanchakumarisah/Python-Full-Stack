#Abstraction for Restaurants
from abc import ABC, abstractmethod #this is used to create abstract classes to implement the abstraction layer
class Dish:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    @abstractmethod
    def prepare_food(self):
        pass
    @abstractmethod
    def get_ingredients(self):
        pass
    def serve_dish(self):
        print("Serving the dish to the customer:", self._name)
    def get_name(self):
        return ("Dish name : ",self._name)
    def get_price(self):
        return ("Dish price : ",self._price)
class pizza(Dish):
    def __init__(self,name,price):
        super().__init__(name, price)
            
    def prepare_food(self):
        print(f"Preparing pizza: {self._name} with price {self._price}")

    def get_ingredients(self):
        return ["Dough", "Tomato Sauce", "Cheese", "Toppings"]
class Resturant:
    def order_dish(self, dish: Dish):
        if dish:
            print("Dish ordered is available.",dish.get_name(),"whose price is: ",dish.get_price())
            dish.get_ingredients()
            dish.prepare_food()
            dish.serve_dish()
        else:
            print("No dish ordered is available.")
        
# Example usage 
lpu_restu = Resturant()
Farm_house=pizza("Farm House", 250)
lpu_restu.order_dish(Farm_house)