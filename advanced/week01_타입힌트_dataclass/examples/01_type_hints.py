def greet(name: str, age: int = 20) -> str:
    return f"{name}({age})"

def add(a: int, b: int) -> int:
    return a + b

count: int = 0
items: list[str] = []
scores: dict[str, int] = {}

print(greet("Alice"))
print(add(3, 5))
