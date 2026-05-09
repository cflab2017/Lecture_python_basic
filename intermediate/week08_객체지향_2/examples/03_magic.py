class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

p = Point(1, 2) + Point(3, 4)
print(p)
print(p == Point(4, 6))
print(p == Point(0, 0))

# set에 넣기
s = {Point(1, 2), Point(1, 2), Point(3, 4)}
print(s)
