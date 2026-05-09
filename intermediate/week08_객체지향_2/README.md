# 8주차. 객체지향 (2) — 상속·다형성·매직 메서드

> 단계: 중급 | 선수: 7주차

## 학습 목표
- 클래스 상속과 `super()` 를 사용한다
- 다형성을 코드로 보인다
- 매직 메서드(`__str__`, `__eq__`, `__add__` 등)를 오버라이딩한다
- 클래스 메서드와 정적 메서드를 구분한다

## 1. 상속

부모 클래스의 속성·메서드를 물려받는다.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):     # Animal 상속
    def speak(self):   # 메서드 오버라이딩
        return "멍멍"

d = Dog("바둑이")
print(d.name, d.speak())   # 바둑이 멍멍
```

## 2. super()

부모의 메서드를 호출.

```python
class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)   # 부모 __init__ 호출
        self.age = age
```

## 3. 다형성

같은 메서드 이름을 다양한 클래스에서 다르게 구현. 호출자는 타입을 신경 쓰지 않음.

```python
animals = [Dog("바둑이"), Cat("나비"), Cow("얼룩이")]
for a in animals:
    print(a.speak())   # 멍멍 / 야옹 / 음매
```

## 4. 매직 메서드

이름이 `__xxx__` 로 시작·끝나는 특별 메서드. 파이썬 문법과 연결됨.

| 메서드 | 트리거 |
|--------|--------|
| `__str__` | `str(x)`, `print(x)` |
| `__repr__` | REPL에서 표시, `repr(x)` |
| `__len__` | `len(x)` |
| `__eq__` | `x == y` |
| `__add__` | `x + y` |
| `__getitem__` | `x[i]` |
| `__iter__` / `__next__` | `for ... in x` |

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

p = Point(1, 2) + Point(3, 4)
print(p)              # Point(4, 6)
print(p == Point(4, 6))   # True
```

## 5. classmethod / staticmethod

```python
class Date:
    def __init__(self, y, m, d):
        self.y, self.m, self.d = y, m, d

    @classmethod
    def from_string(cls, s):
        y, m, d = map(int, s.split("-"))
        return cls(y, m, d)        # 인스턴스 생성

    @staticmethod
    def is_valid(y, m, d):
        return 1 <= m <= 12 and 1 <= d <= 31

print(Date.from_string("2026-05-09").y)
print(Date.is_valid(2026, 5, 9))
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_inherit.py` | 상속과 super |
| `02_polymorphism.py` | 다형성 |
| `03_magic.py` | 매직 메서드 |
| `04_classmethod.py` | classmethod/staticmethod |

## ⚠️ 자주 하는 실수

1. **`super().__init__()` 누락** — 부모 속성이 초기화 안 됨.
2. **매직 메서드를 일반 호출** — `p.add(q)` 가 아니라 `p + q`.
3. **`__eq__` 만 만들고 `__hash__` 빼먹음** — set/dict 키로 못 씀. `__hash__` 도 일관되게 정의.
4. **다중 상속 남용** — 가능하지만 복잡. 가능하면 컴포지션.

## ❓ FAQ

**Q1. 추상 클래스(인터페이스) 만들려면?**
A. `abc.ABC` 와 `@abstractmethod` 사용.

**Q2. `__str__` vs `__repr__` ?**
A. `__str__` 은 사람용, `__repr__` 은 개발자용 (디버깅). 보통 `__repr__` 만 정의해도 됨.

**Q3. 상속 vs 컴포지션?**
A. "is-a" 관계면 상속, "has-a" 면 속성 보유 (컴포지션). 의심되면 컴포지션.

## 📝 과제 (exercises/)

- `exercise1.md` — `Shape` 추상 → `Rectangle`, `Circle`
- `exercise2.md` — `Playlist` 클래스 + 매직 메서드
- `exercise3.md` — `Vector` 클래스 (+, -, ==, repr)

## 다음 주차

[9주차. 정규표현식](../week09_정규표현식/)
