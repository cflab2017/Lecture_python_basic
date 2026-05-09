# 파이썬 강의 - 기초 과정

> 본 과정은 **기초 / 중급 / 고급** 3단계 커리큘럼 중 **기초** 단계입니다.
> 모든 주차는 **예제 중심**으로 진행하며, 매 주차마다 **과제**를 부여합니다.

## 강의 개요

- **대상**: 프로그래밍을 처음 시작하는 입문자
- **기간**: 총 10주 (주 1회, 회당 2시간 / 총 20시간)
- **선수 지식**: 없음
- **수업 방식**:
  - 이론 설명 30%, 라이브 코딩 예제 40%, 실습 30%
  - 매 주차 **3~5개의 핵심 예제** 직접 작성
  - 매 주차 **과제 1~2개** 제출

---

## 주차별 커리큘럼

### 1주차. 파이썬 시작하기

**학습 목표**: 환경 설정 → 첫 코드 실행 → 기본 출력까지

**핵심 예제**

```python
# 예제 1. 첫 출력
print("Hello, Python!")

# 예제 2. 여러 줄 출력
print("이름: 홍길동")
print("나이: 20")

# 예제 3. 주석과 한글 출력
# 이것은 한 줄 주석입니다
print("안녕하세요, 파이썬!")
```

**과제**
1. VS Code + Python 설치 후 스크린샷 제출
2. 본인의 이름, 나이, 좋아하는 언어를 출력하는 `intro.py` 작성
3. `print` 문 5개 이상을 사용한 자기소개 카드 출력

---

### 2주차. 변수와 자료형

**학습 목표**: 자료형을 구분하고 형 변환을 사용할 수 있다

**핵심 예제**

```python
# 예제 1. 변수 선언
name = "홍길동"
age = 20
height = 175.5
is_student = True

# 예제 2. 타입 확인
print(type(name), type(age), type(height), type(is_student))

# 예제 3. 형 변환
num_str = "123"
num_int = int(num_str)
print(num_int + 7)   # 130

# 예제 4. 잘못된 형 변환 (오류 관찰)
# int("abc")  # ValueError
```

**과제**
1. 사용자 이름과 출생연도를 입력받아 만 나이를 출력하는 프로그램
2. 5개 이상의 변수를 선언하고 각 타입을 출력하는 코드
3. 정수, 실수, 문자열, 불리언을 한 번씩 사용하는 짧은 프로그램

---

### 3주차. 연산자와 입출력

**학습 목표**: 사칙연산과 사용자 입력으로 동작하는 프로그램을 만든다

**핵심 예제**

```python
# 예제 1. 산술 연산자
print(7 // 2, 7 % 2, 2 ** 10)   # 3 1 1024

# 예제 2. input()
name = input("이름을 입력하세요: ")
print(f"{name}님 환영합니다!")

# 예제 3. f-string 포맷
price = 12345
print(f"가격: {price:,}원")        # 12,345원
print(f"원주율: {3.141592:.2f}")   # 3.14

# 예제 4. 입력값을 숫자로 변환
a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))
print(f"{a} + {b} = {a + b}")
```

**과제**
1. **BMI 계산기**: 키(cm)와 몸무게(kg)를 입력받아 BMI 값을 소수점 둘째 자리까지 출력
2. **거스름돈 계산기**: 결제 금액과 받은 돈을 입력받아 거스름돈 출력
3. **간단 환율 변환기**: 원화를 입력받아 달러로 변환 (환율은 상수로 고정)

---

### 4주차. 조건문

**학습 목표**: 조건에 따라 다른 동작을 수행하는 코드를 작성한다

**핵심 예제**

```python
# 예제 1. if / elif / else
score = int(input("점수: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"학점: {grade}")

# 예제 2. 논리 연산자
age = int(input("나이: "))
if age >= 13 and age <= 18:
    print("청소년 요금")

# 예제 3. 조건 표현식
n = int(input("숫자: "))
result = "짝수" if n % 2 == 0 else "홀수"
print(result)
```

**과제**
1. **학점 계산기**: 점수 입력 → A/B/C/D/F 출력 (90/80/70/60 기준)
2. **윤년 판별기**: 연도를 입력받아 윤년 여부 출력 (4의 배수 & (100의 배수 아님 or 400의 배수))
3. **가위바위보**: 사용자 입력 vs 컴퓨터(`random`) 비교 후 승/패/무 출력

---

### 5주차. 반복문

**학습 목표**: `for`/`while`로 반복 작업을 자동화한다

**핵심 예제**

```python
# 예제 1. for + range
for i in range(1, 11):
    print(i, end=" ")   # 1 2 3 ... 10

# 예제 2. 합계 구하기
total = 0
for i in range(1, 101):
    total += i
print(total)   # 5050

# 예제 3. while
n = 1
while n <= 5:
    print("*" * n)
    n += 1

# 예제 4. break / continue
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i, end=" ")   # 1 2 3 4 6 7
```

**과제**
1. **구구단**: 2단~9단을 출력하는 프로그램 (이중 반복문)
2. **별 찍기**: 직각 삼각형, 역삼각형, 다이아몬드 중 2개 구현
3. **숫자 맞추기 게임**: 1~100 사이 랜덤 숫자를 사용자가 맞추도록, 시도 횟수 표시

---

### 6주차. 리스트와 튜플

**학습 목표**: 여러 개의 값을 리스트/튜플로 다룰 수 있다

**핵심 예제**

```python
# 예제 1. 리스트 기본
fruits = ["사과", "바나나", "포도"]
print(fruits[0], fruits[-1])
fruits.append("딸기")
fruits.remove("바나나")

# 예제 2. 슬라이싱
nums = [10, 20, 30, 40, 50]
print(nums[1:4])     # [20, 30, 40]
print(nums[::-1])    # [50, 40, 30, 20, 10]

# 예제 3. 순회 + enumerate
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}번: {fruit}")

# 예제 4. 튜플 언패킹
point = (10, 20)
x, y = point
print(x, y)
```

**과제**
1. **학생 점수 관리**: 5명의 점수를 리스트에 저장 → 총점, 평균, 최고/최저점 출력
2. **로또 번호 생성기**: 1~45 중 중복 없이 6개를 뽑아 정렬 후 출력
3. **리스트 뒤집기**: 슬라이싱과 `reverse()` 두 가지 방식으로 구현 비교

---

### 7주차. 딕셔너리와 집합

**학습 목표**: 키-값 구조와 집합 연산을 활용한다

**핵심 예제**

```python
# 예제 1. 딕셔너리 기본
student = {"name": "홍길동", "age": 20, "major": "CS"}
print(student["name"])
student["age"] = 21
student["email"] = "hong@example.com"

# 예제 2. get과 순회
for key, value in student.items():
    print(f"{key}: {value}")

print(student.get("phone", "없음"))   # 안전하게 조회

# 예제 3. 집합 연산
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)   # 합집합
print(a & b)   # 교집합
print(a - b)   # 차집합

# 예제 4. 단어 빈도 카운트
text = "apple banana apple grape banana apple"
count = {}
for word in text.split():
    count[word] = count.get(word, 0) + 1
print(count)   # {'apple': 3, 'banana': 2, 'grape': 1}
```

**과제**
1. **연락처 프로그램**: 이름→전화번호 딕셔너리에 추가/조회/삭제 기능 구현
2. **단어 빈도 카운터**: 문장을 입력받아 가장 많이 나온 단어 Top 3 출력
3. **중복 제거**: 리스트에서 중복을 제거하되 입력 순서를 유지

---

### 8주차. 문자열 다루기

**학습 목표**: 문자열 메서드와 포맷팅을 자유롭게 사용한다

**핵심 예제**

```python
# 예제 1. 자주 쓰는 메서드
s = "  Hello, Python!  "
print(s.strip())             # 양쪽 공백 제거
print(s.lower())
print(s.replace("Python", "World"))

# 예제 2. split / join
csv = "사과,바나나,포도"
fruits = csv.split(",")
print(fruits)
print(" / ".join(fruits))    # 사과 / 바나나 / 포도

# 예제 3. 슬라이싱
email = "user@example.com"
id_part = email[:email.index("@")]
print(id_part)               # user

# 예제 4. f-string 정렬
for name, score in [("Alice", 92), ("Bob", 78), ("Charlie", 100)]:
    print(f"{name:<10}{score:>5}점")
```

**과제**
1. **회문(palindrome) 판별**: 입력 문자열이 앞뒤가 같은지 확인 ("기러기" → True)
2. **이메일 검증**: `@`와 `.`을 모두 포함하는지 검사
3. **텍스트 통계**: 문장을 입력받아 전체 글자 수, 단어 수, 평균 단어 길이 출력

---

### 9주차. 함수 기초

**학습 목표**: 코드를 함수로 분리하여 재사용 가능하게 만든다

**핵심 예제**

```python
# 예제 1. 함수 정의
def add(a, b):
    return a + b

print(add(3, 5))   # 8

# 예제 2. 기본값 매개변수
def greet(name, greeting="안녕"):
    return f"{greeting}, {name}님!"

print(greet("길동"))                 # 안녕, 길동님!
print(greet("Alice", "Hello"))       # Hello, Alice님!

# 예제 3. 여러 값 반환 (튜플)
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(lo, hi)   # 1 9

# 예제 4. 스코프
total = 0
def add_to_total(x):
    global total
    total += x

add_to_total(10)
add_to_total(20)
print(total)   # 30
```

**과제**
1. **계산기 함수 모음**: `add`, `sub`, `mul`, `div` 함수를 만들고 메뉴 선택형 계산기 구현
2. **입력 검증 함수**: `is_valid_age(value)` — 0~120 사이 정수면 True 반환
3. **소수 판별 함수**: `is_prime(n)` 작성 후 1~50 중 소수만 출력

---

### 10주차. 기초 종합 프로젝트

**학습 목표**: 지금까지 배운 내용을 통합해 하나의 작은 프로그램을 완성한다

**핵심 예제**: 미니 To-Do List 골격

```python
todos = []

def add(task):
    todos.append({"task": task, "done": False})

def show():
    for i, t in enumerate(todos, 1):
        mark = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {mark} {t['task']}")

def done(idx):
    todos[idx - 1]["done"] = True

while True:
    cmd = input("명령(add/show/done/quit): ").strip()
    if cmd == "quit":
        break
    elif cmd == "add":
        add(input("할 일: "))
    elif cmd == "show":
        show()
    elif cmd == "done":
        done(int(input("번호: ")))
```

**과제 (택 1, 최종 제출)**
1. **콘솔 To-Do List**: 추가/조회/완료/삭제 기능
2. **단어장 퀴즈**: 영단어-뜻 딕셔너리로 랜덤 퀴즈 출제, 점수 집계
3. **가계부**: 수입/지출 기록, 카테고리별 합계, 잔액 출력
4. **숫자 야구**: 3자리 숫자 맞히기 (스트라이크/볼)

**제출물**
- `.py` 소스 파일
- 간단한 설명 README (실행법, 사용한 문법)
- 시연 스크린샷 또는 녹화

---

## 평가 방식

| 항목 | 비중 |
|------|------|
| 출석 | 10% |
| 주차별 과제 (1~9주차) | 40% |
| 중간 퀴즈 (5주차) | 20% |
| 최종 프로젝트 (10주차) | 30% |

**과제 채점 기준**
- 정확성 (요구사항 충족) — 50%
- 가독성 (변수명, 들여쓰기, 분리) — 25%
- 응용력 (추가 기능, 예외 케이스 처리) — 25%

---

## 다음 단계

- **중급 과정**: 함수 심화, 모듈/패키지, 객체지향, 예외 처리, 파일 입출력, 컴프리헨션·제너레이터
- **고급 과정**: 데코레이터, 타입 힌트, 동시성(asyncio), 테스트, 외부 라이브러리(NumPy/Pandas/Requests), 패키징·배포

---

## 추천 학습 자료

- [Python 공식 튜토리얼 (한국어)](https://docs.python.org/ko/3/tutorial/)
- [점프 투 파이썬](https://wikidocs.net/book/1)
- 연습: [백준 단계별 풀이](https://www.acmicpc.net/step), [프로그래머스 입문](https://school.programmers.co.kr)
