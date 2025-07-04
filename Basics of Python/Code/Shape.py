class Shape:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side * self.side

def print_area(shape):
    print(f"Shape Color: {shape.get_color()}, Area: {shape.area()}")

# Example usage
circle1 = Circle("Red", 5)
square1 = Square("Blue", 4)
print_area(circle1)  # Shape Color: Red, Area: 78.5
print_area(square1)  # Shape Color: Blue, Area: 16
