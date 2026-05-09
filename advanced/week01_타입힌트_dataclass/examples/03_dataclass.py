from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)
print(p == Point(1, 2))
print(p == Point(1, 3))

@dataclass
class User:
    name: str
    age: int = 20   # 기본값

u = User("Alice")
print(u)
