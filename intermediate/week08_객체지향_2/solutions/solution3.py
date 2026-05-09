import math

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)
print(v1 - v2)
print(v1.magnitude())
print(v1 == Vector(3, 4))
