# 파이썬 강의 - 중급 과정

> 본 과정은 **기초 / 중급 / 고급 / 실습과제** 4단계 커리큘럼 중 **2단계 (중급)** 입니다.
> 모든 주차는 **예제 중심**으로 진행하며, 매 주차마다 **과제**를 부여합니다.

## 강의 개요

- **대상**: 기초 과정을 이수한 학습자
- **기간**: 총 10주 (주 1회, 회당 2시간 / 총 20시간)
- **선수 지식**: 기초 과정 (자료형, 조건/반복문, 자료구조, 함수 기초)
- **수업 방식**:
  - 이론 설명 30%, 라이브 코딩 예제 40%, 실습 30%
  - 매 주차 **3~4개의 핵심 예제** 직접 작성
  - 매 주차 **과제 2~3개** 제출
- **학습 목표**:
  - 함수형 도구(람다·클로저·고차함수)를 이해하고 활용한다
  - 모듈과 패키지로 프로젝트를 구조화할 수 있다
  - 예외 처리로 견고한 프로그램을 작성할 수 있다
  - 텍스트·CSV·JSON 파일을 자유롭게 다룬다
  - 객체지향 프로그래밍의 핵심 개념을 코드로 구현한다
  - 정규표현식으로 텍스트 패턴을 매칭한다

---

## 주차별 커리큘럼

### 1주차. 함수 심화

**학습 목표**: 가변 인자, 람다, 고차함수를 활용한다

**핵심 예제**

```python
# 예제 1. *args, **kwargs
def log(*args, **kwargs):
    print("위치 인자:", args)
    print("키워드 인자:", kwargs)

log(1, 2, 3, name="홍길동", age=20)

# 예제 2. 람다와 고차함수
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * x, nums)))      # [1, 4, 9, 16, 25]
print(list(filter(lambda x: x % 2, nums)))   # [1, 3, 5]

# 예제 3. 정렬 키
people = [("Alice", 30), ("Bob", 25), ("Charlie", 28)]
people.sort(key=lambda p: p[1])
print(people)

# 예제 4. 클로저
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = counter()
print(c(), c(), c())   # 1 2 3
```

**과제**
1. 가변 인자로 평균/분산을 계산하는 함수 `stats(*nums)` 작성
2. `sort(key=...)` 로 학생 리스트를 점수 기준 내림차순 정렬
3. 호출 횟수를 누적하는 클로저 만들기 (`make_counter`)

---

### 2주차. 컴프리헨션과 제너레이터

**학습 목표**: 컴프리헨션과 제너레이터로 간결하고 효율적인 코드 작성

**핵심 예제**

```python
# 예제 1. 리스트 컴프리헨션
squares = [x * x for x in range(10) if x % 2 == 0]
print(squares)   # [0, 4, 16, 36, 64]

# 예제 2. 딕셔너리/집합 컴프리헨션
words = ["apple", "banana", "apple", "cherry"]
length_map = {w: len(w) for w in set(words)}
print(length_map)

# 예제 3. 제너레이터 함수
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fib(10)))

# 예제 4. 제너레이터 표현식 (메모리 절약)
total = sum(x * x for x in range(1_000_000))
print(total)
```

**과제**
1. 1~100 중 소수만 골라내는 리스트 컴프리헨션
2. 단어 리스트에서 `{단어: 길이}` 딕셔너리 생성
3. `read_lines(path)` 제너레이터로 큰 파일을 한 줄씩 읽기

---

### 3주차. 모듈과 패키지

**학습 목표**: 코드를 모듈/패키지로 분리해 재사용한다

**핵심 예제**

```python
# 예제 1. 자체 모듈 만들기 (calc.py)
# calc.py
def add(a, b): return a + b
def sub(a, b): return a - b

# main.py
import calc
from calc import add
print(calc.add(1, 2), add(3, 4))

# 예제 2. __name__ == "__main__" 패턴
def main():
    print("스크립트로 실행됨")

if __name__ == "__main__":
    main()

# 예제 3. 패키지 구조
# mypkg/
# ├── __init__.py
# ├── math_utils.py
# └── string_utils.py
from mypkg.math_utils import add
from mypkg.string_utils import slugify
```

**과제**
1. `calculator/` 패키지 생성: `basic.py`(사칙연산) + `advanced.py`(제곱·루트), `__init__.py`에서 통합 export
2. `string_utils.py` 모듈을 만들고 `slugify`, `truncate` 함수 작성
3. `__name__ == "__main__"` 으로 모듈을 라이브러리/스크립트 양쪽으로 사용

---

### 4주차. 표준 라이브러리 활용

**학습 목표**: 자주 쓰는 표준 라이브러리를 손에 익힌다

**핵심 예제**

```python
# 예제 1. datetime
from datetime import datetime, timedelta
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))
print(now + timedelta(days=7))

# 예제 2. random
import random
print(random.randint(1, 100))
print(random.sample(range(1, 46), 6))   # 로또

# 예제 3. pathlib
from pathlib import Path
p = Path("data") / "report.txt"
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("hello", encoding="utf-8")
print(p.read_text(encoding="utf-8"))

# 예제 4. collections
from collections import Counter, defaultdict
text = "to be or not to be"
print(Counter(text.split()))   # Counter({'to': 2, 'be': 2, ...})
```

**과제**
1. `datetime` 으로 D-Day 계산기 (목표일까지 남은 일수)
2. `pathlib` 으로 폴더 내 모든 `.txt` 파일 목록과 크기 출력
3. `Counter` 로 문장에서 가장 많이 등장한 단어 Top 5 구하기

---

### 5주차. 예외 처리

**학습 목표**: 예외를 처리해 프로그램이 죽지 않도록 만든다

**핵심 예제**

```python
# 예제 1. 기본 try/except
try:
    n = int(input("숫자: "))
    print(10 / n)
except ValueError:
    print("숫자가 아닙니다")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")

# 예제 2. else / finally
try:
    f = open("data.txt", encoding="utf-8")
except FileNotFoundError:
    print("파일이 없습니다")
else:
    print(f.read())
    f.close()
finally:
    print("정리 완료")

# 예제 3. 예외 발생시키기
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("잔액 부족")
    return balance - amount

# 예제 4. 사용자 정의 예외
class InsufficientFundsError(Exception):
    pass

def transfer(account, amount):
    if account.balance < amount:
        raise InsufficientFundsError(f"잔액 {account.balance} < 요청 {amount}")
```

**과제**
1. 안전한 정수 입력 함수 `read_int(prompt)` — 잘못 입력 시 다시 받기
2. 사용자 정의 예외 `InvalidScoreError` 만들고 0~100 범위 검증
3. 파일 읽기 함수에 `FileNotFoundError`, `PermissionError` 분기 처리

---

### 6주차. 파일 입출력 (텍스트·CSV·JSON)

**학습 목표**: 외부 데이터를 읽고 쓰는 프로그램을 만든다

**핵심 예제**

```python
# 예제 1. 텍스트 with 문
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("첫 줄\n둘째 줄\n")

with open("notes.txt", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())

# 예제 2. CSV 읽기/쓰기
import csv
with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "score"])
    w.writerows([["Alice", 92], ["Bob", 78]])

with open("scores.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["score"])

# 예제 3. JSON
import json
data = {"name": "홍길동", "skills": ["Python", "SQL"]}
with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("profile.json", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["skills"])
```

**과제**
1. `notes.txt` 에 메모를 추가하고 전체 내용을 보여주는 메모장
2. CSV로 저장된 학생 점수를 읽어 평균/표준편차 출력
3. JSON 파일에 To-Do 리스트를 저장/불러오기 (영구 보존)

---

### 7주차. 객체지향 프로그래밍 (1)

**학습 목표**: 클래스, 인스턴스, 캡슐화 개념을 코드로 구현한다

**핵심 예제**

```python
# 예제 1. 클래스 기본
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액 부족")
        self.balance -= amount

a = Account("홍길동", 1000)
a.deposit(500)
print(a.balance)   # 1500

# 예제 2. 캡슐화 (관례적 _, __ )
class Account:
    def __init__(self, owner, balance):
        self._owner = owner
        self.__balance = balance   # name mangling

    def get_balance(self):
        return self.__balance

# 예제 3. 클래스 변수 vs 인스턴스 변수
class Counter:
    total = 0   # 클래스 변수
    def __init__(self):
        Counter.total += 1
        self.id = Counter.total

print(Counter().id, Counter().id, Counter.total)   # 1 2 2
```

**과제**
1. `BankAccount` 클래스: 입금/출금/잔액 조회, 잔액 부족 시 예외
2. `Stack` 클래스: `push`, `pop`, `peek`, `is_empty` 메서드 구현
3. `Student` 클래스: 이름·점수 리스트 → 평균·최고점 메서드

---

### 8주차. 객체지향 프로그래밍 (2)

**학습 목표**: 상속, 다형성, 매직 메서드를 활용한다

**핵심 예제**

```python
# 예제 1. 상속과 super()
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "멍멍"

class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

# 예제 2. 다형성
animals = [Dog("바둑이"), Animal("?")]
for a in animals:
    print(a.name, a.speak())

# 예제 3. 매직 메서드
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
print(p)   # Point(4, 6)
```

**과제**
1. `Shape` 추상 → `Rectangle`, `Circle` 구현, 공통 인터페이스 `area()`
2. 매직 메서드 `__len__`, `__getitem__` 으로 `Playlist` 클래스 구현
3. `Vector` 클래스: `+`, `-`, `==`, `__repr__` 오버로딩

---

### 9주차. 정규표현식

**학습 목표**: `re` 모듈로 텍스트 패턴을 매칭·추출한다

**핵심 예제**

```python
import re

# 예제 1. 기본 매칭
m = re.search(r"\d{3}-\d{4}-\d{4}", "전화: 010-1234-5678")
print(m.group())   # 010-1234-5678

# 예제 2. findall, sub
text = "사과 5개, 바나나 3개, 포도 12개"
print(re.findall(r"\d+", text))            # ['5', '3', '12']
print(re.sub(r"\d+", "?", text))            # 사과 ?개, 바나나 ?개, 포도 ?개

# 예제 3. 그룹 캡처
log = "ERROR 2026-05-09 14:32 사용자 인증 실패"
m = re.match(r"(\w+) (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) (.+)", log)
print(m.groups())

# 예제 4. 컴파일
email_re = re.compile(r"[\w.]+@[\w.]+\.\w+")
print(email_re.findall("문의: a@b.com, c@d.co.kr"))
```

**과제**
1. 문자열에서 모든 이메일 추출
2. 휴대폰 번호 형식(`010-XXXX-XXXX`) 검증 함수
3. 로그에서 ERROR 라인만 추출하고 시각만 출력

---

### 10주차. 중급 종합 실습

**학습 목표**: 지금까지 배운 내용을 통합한 미니 프로젝트 구현

**핵심 예제 (단어장 앱 골격)**

```python
import json
from pathlib import Path

DB = Path("words.json")

class Word:
    def __init__(self, en, ko):
        self.en, self.ko = en, ko
    def to_dict(self):
        return {"en": self.en, "ko": self.ko}

class WordBook:
    def __init__(self, path):
        self.path = path
        self.words = self._load()

    def _load(self):
        if not self.path.exists():
            return []
        return [Word(**w) for w in json.loads(self.path.read_text(encoding="utf-8"))]

    def save(self):
        data = [w.to_dict() for w in self.words]
        self.path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def add(self, en, ko):
        self.words.append(Word(en, ko))
        self.save()
```

**과제 (택 1, 최종 제출)**
1. **단어장 앱**: 단어 추가/삭제/검색, JSON 저장, 퀴즈 모드
2. **간이 가계부**: 수입·지출 기록(JSON), 카테고리별 합계
3. **로그 분석기**: 텍스트 로그 파일 → 정규식으로 ERROR/WARN 분리, CSV 리포트
4. **연락처 관리자 (OOP)**: `Contact`, `AddressBook` 클래스, 파일 영구화

**제출물**
- 모듈 분리된 패키지 구조
- 예외 처리 및 사용자 친화적 메시지
- README (실행법, 사용한 문법)

---

## 평가 방식

| 항목 | 비중 |
|------|------|
| 출석 | 10% |
| 주차별 과제 (1~9주차) | 40% |
| 중간 퀴즈 (5주차) | 20% |
| 최종 프로젝트 (10주차) | 30% |

**과제 채점 기준**
- 정확성 (요구사항 충족) — 40%
- 가독성 / 모듈 분리 — 25%
- 예외 처리 — 15%
- 응용·도전 — 20%

---

## 다음 단계

중급을 마치면 **고급 과정**으로 진행합니다.

- 7~8주차 OOP → 고급 1주차 타입 힌트 + dataclass
- 5주차 예외 처리 → 고급 2주차 컨텍스트 매니저
- 6주차 파일 I/O → 고급 7주차 웹 스크래핑

병행 추천: **실습과제 Lv ★★★** (가계부, 도서 관리, 일기장, 텍스트 어드벤처)

---

## 추천 학습 자료

- [Fluent Python (한빛미디어)](https://www.hanbit.co.kr/store/books/look.php?p_code=B4097515591)
- [Real Python](https://realpython.com)
- [Python 공식 라이브러리 레퍼런스](https://docs.python.org/ko/3/library/)
- 연습: [프로그래머스 Lv 1~2](https://school.programmers.co.kr), [LeetCode Easy](https://leetcode.com)
