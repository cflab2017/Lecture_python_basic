# 1주차. 타입 힌트와 dataclass

> 단계: 고급 | 선수: 중급 7-8주차 (OOP)

## 학습 목표
- 타입 힌트 문법을 익힌다 (`int`, `str`, `list[int]`, `Optional`)
- `mypy` 로 정적 타입 검사한다
- `@dataclass` 로 데이터 클래스를 간결하게 작성한다
- `field(default_factory=list)` 함정을 안다

## 1. 타입 힌트 기본

런타임에는 영향 없지만, IDE 자동완성·정적 분석·문서화에 큰 도움.

```python
def greet(name: str, age: int = 20) -> str:
    return f"{name}({age})"

count: int = 0
items: list[str] = []
```

## 2. typing 모듈

```python
from typing import Optional, Union, Any, Callable

def find_user(uid: int) -> Optional[dict]:
    """Optional[X] = X | None"""
    ...

def parse(value: Union[str, int]) -> int:
    """str 또는 int (Python 3.10+ 에서는 str | int)"""
    ...

handler: Callable[[int], str] = lambda x: str(x)
```

Python 3.10+ 부터:
```python
def find_user(uid: int) -> dict | None: ...
def parse(value: str | int) -> int: ...
```

## 3. 컨테이너 타입

```python
nums: list[int] = [1, 2, 3]
scores: dict[str, int] = {"Alice": 90}
pair: tuple[int, str] = (1, "a")
unique: set[int] = {1, 2, 3}
```

## 4. mypy

```bash
pip install mypy
mypy main.py
mypy --strict main.py    # 엄격 모드
```

## 5. dataclass

`__init__`, `__repr__`, `__eq__` 자동 생성.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)              # Point(x=1, y=2) — __repr__ 자동
print(p == Point(1, 2))   # True — __eq__ 자동
```

## 6. dataclass 옵션

```python
from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    author: str
    tags: list[str] = field(default_factory=list)   # 가변 기본값
    price: float = 0.0

b = Book("Python", "Guido")
b.tags.append("language")
```

⚠️ `tags: list[str] = []` 는 **모든 인스턴스가 공유** — 절대 안 됨. 반드시 `field(default_factory=list)`.

## 7. frozen dataclass

불변 객체. 해시 가능 → set/dict 키.

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
# p.x = 99   # FrozenInstanceError
{Point(1, 2)}   # OK
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_type_hints.py` | 기본 타입 힌트 |
| `02_typing_module.py` | Optional, Union, Callable |
| `03_dataclass.py` | dataclass 기본 |
| `04_dataclass_advanced.py` | field, frozen |

## ⚠️ 자주 하는 실수

1. **가변 기본값을 그대로** — `field(default_factory=list)` 사용
2. **`Optional` 의미 오해** — `Optional[int]` = `int | None`. 단순히 "선택적 인자" 가 아님
3. **타입 힌트가 런타임에 검증된다고 오해** — 그냥 힌트일 뿐. 런타임 검증은 `pydantic` 같은 별도 라이브러리

## ❓ FAQ

**Q1. 타입 힌트를 다 달아야 하나요?**
A. 공개 API(함수 시그니처)는 강력 권장. 내부 변수는 추론으로 충분.

**Q2. `dataclass` vs `pydantic.BaseModel` 차이?**
A. dataclass는 표준, pydantic은 런타임 검증·직렬화 강력. 데이터 처리 많으면 pydantic.

**Q3. `Any` 를 쓰면 어떻게 되나요?**
A. mypy가 검사를 포기. 가능하면 더 구체적인 타입.

## 📝 과제 (exercises/)

- `exercise1.md` — 중급 코드에 타입 힌트 추가
- `exercise2.md` — `Book/Member/Loan` dataclass
- `exercise3.md` — Optional/list/dict 시그니처 5개

## 다음 주차

[2주차. 데코레이터와 컨텍스트 매니저](../week02_데코레이터_컨텍스트매니저/)
