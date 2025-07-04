#Create a class Appliance with brand and power consumption. Inherit Fan, AC,
#  and Heater classes from it, each with a method show_details()
#  displaying their specific features and inherited ones.
class Application:
    def __init__(self, brand, power_consumption):
        self.brand = brand
        self.power_consumption = power_consumption

    def show_details(self):
        print("brand:", self.brand)
        print("power consumption:", self.power_consumption)
class Fan(Application):
    def __init__(self, brand, power_consumption, blade_size):
        super().__init__(brand, power_consumption)
        self.blade_size = blade_size

    def show_details(self):
        super().show_details()
        print("blade size:", self.blade_size)

class AC(Application):
    def __init__(self, brand, power_consumption, cooling_capacity):
        super().__init__(brand, power_consumption)
        self.cooling_capacity = cooling_capacity

    def show_details(self):
        super().show_details()
        print("cooling capacity:", self.cooling_capacity)

class Heater(Application):
    def __init__(self, brand, power_consumption, heating_capacity):
        super().__init__(brand, power_consumption)
        self.heating_capacity = heating_capacity

    def show_details(self):
        super().show_details()
        print("heating capacity:", self.heating_capacity)
# Creating objects of each class
fan = Fan("CoolAir", "75W", "16 inches")
ac = AC("CoolBreeze", "1500W", "2 tons")
heater = Heater("WarmHome", "1000W", "3 kW")    
# Calling show_details method for each object
fan.show_details()
print()  # For better readability
ac.show_details()   
print()  # For better readability
heater.show_details()
print()  # For better readability