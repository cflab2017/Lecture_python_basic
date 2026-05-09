import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimeter(self): ...

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
    def __repr__(self):
        return f"Circle({self.radius})"

shapes = [Rectangle(3, 4), Circle(5)]
for s in shapes:
    print(f"{s} → 면적: {s.area():.2f}, 둘레: {s.perimeter():.2f}")
