# 7주차. 객체지향 프로그래밍 (1) — 클래스와 인스턴스

> 단계: 중급 | 선수: 6주차

## 학습 목표
- 클래스를 정의하고 인스턴스를 만든다
- `__init__` 생성자와 `self` 의 의미를 이해한다
- 인스턴스 메서드와 속성을 다룬다
- 캡슐화 관례 (`_`, `__`)

## 1. 클래스란

데이터(속성)와 동작(메서드)을 묶은 설계도. 이를 바탕으로 만든 게 인스턴스(객체).

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner       # 인스턴스 속성
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액 부족")
        self.balance -= amount

a = Account("홍길동", 1000)    # 인스턴스 생성
a.deposit(500)
print(a.balance)   # 1500
```

## 2. self 의 의미

메서드의 첫 인자는 항상 `self` — **호출된 인스턴스 자신**.

```python
a = Account("홍길동")
a.deposit(100)        # 실제로는 Account.deposit(a, 100)
```

`self` 를 통해 인스턴스 속성에 접근.

## 3. 인스턴스 변수 vs 클래스 변수

```python
class Counter:
    total = 0   # 클래스 변수 — 모든 인스턴스가 공유

    def __init__(self):
        Counter.total += 1
        self.id = Counter.total   # 인스턴스 변수 — 각자 다름

c1 = Counter()
c2 = Counter()
print(c1.id, c2.id, Counter.total)   # 1 2 2
```

## 4. 캡슐화 관례

파이썬은 진짜 private이 없습니다. 관례로 표현:
- `_var` — "내부용" (외부에서 쓰지 말라는 신호)
- `__var` — name mangling (`_ClassName__var` 로 변환됨)

```python
class Account:
    def __init__(self, owner, balance):
        self._owner = owner       # 내부용
        self.__balance = balance  # name mangled

    def get_balance(self):
        return self.__balance

a = Account("홍길동", 1000)
print(a._owner)              # 가능 (관례로 자제)
# print(a.__balance)         # AttributeError
print(a._Account__balance)   # 동작은 함 (권장 X)
```

## 5. 객체 비교

기본 `==` 은 같은 객체인지 (id 비교). 의미적 비교는 `__eq__` 오버라이딩 필요 (다음 주차).

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_class_basic.py` | 클래스 정의·인스턴스 |
| `02_self.py` | self 의 동작 |
| `03_class_var.py` | 클래스 변수 vs 인스턴스 변수 |
| `04_encapsulation.py` | 캡슐화 관례 |

## ⚠️ 자주 하는 실수

1. **`self` 빠뜨림** — `def deposit(amount):` → 자동으로 인스턴스가 들어가는데 매개변수 없으면 TypeError.
2. **클래스 변수에 가변 객체** — 모든 인스턴스가 공유돼서 의도치 않게 같이 변함.
   ```python
   class Bag:
       items = []   # 위험!
   ```
   → `__init__` 안에서 `self.items = []`.
3. **`__init__` 에서 다른 이름의 속성 사용** — 오타로 인한 attribute 누락.

## ❓ FAQ

**Q1. 모든 코드를 클래스로 짜야 하나요?**
A. 아닙니다. **상태 + 동작이 묶여야 의미 있을 때만**. 단순 함수가 더 명확하면 함수.

**Q2. `__init__` 외에 다른 매직 메서드는?**
A. 다음 주차에서 `__str__`, `__eq__`, `__len__` 등 학습.

**Q3. 클래스 이름 명명 규칙은?**
A. **PascalCase** (`BankAccount`, `UserProfile`). 함수·변수는 snake_case.

## 📝 과제 (exercises/)

- `exercise1.md` — `BankAccount` 클래스
- `exercise2.md` — `Stack` 클래스
- `exercise3.md` — `Student` 클래스 (점수 평균/최고)

## 다음 주차

[8주차. 객체지향 (2)](../week08_객체지향_2/) — 상속·다형성
