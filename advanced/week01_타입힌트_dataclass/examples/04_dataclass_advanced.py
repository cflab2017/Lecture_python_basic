from dataclasses import dataclass, field, asdict

@dataclass
class Book:
    title: str
    author: str
    tags: list[str] = field(default_factory=list)
    price: float = 0.0

b = Book("Python", "Guido")
b.tags.append("language")
print(b)
print(asdict(b))   # 딕셔너리로 변환

# frozen — 불변
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
print({p, Point(1, 2), Point(3, 4)})   # set에 들어감

try:
    p.x = 99
except Exception as e:
    print("frozen 에러:", e)
