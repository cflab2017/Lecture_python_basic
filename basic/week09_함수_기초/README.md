# 9주차. 함수 기초

> 단계: 기초 | 선수: 8주차 (지금까지의 모든 문법)

## 학습 목표
- `def` 로 함수를 정의하고 호출한다
- 매개변수와 인수의 차이를 안다
- 기본값 매개변수, 키워드 인수를 사용한다
- `return` 으로 값을 반환한다
- 변수의 스코프(지역/전역)를 이해한다

## 1. 함수란

같은 동작을 여러 번 쓰지 않고 **이름 붙여 재사용**. 코드를 짧고 명확하게 만든다.

```python
def greet(name):
    print(f"안녕, {name}!")

greet("홍길동")
greet("김영희")
```

## 2. 매개변수와 인수

- **매개변수(parameter)**: 함수 정의의 변수 (`name`)
- **인수(argument)**: 함수 호출 시 전달하는 값 (`"홍길동"`)

```python
def add(a, b):       # a, b: 매개변수
    return a + b

result = add(3, 5)   # 3, 5: 인수
```

## 3. return

함수가 값을 돌려줍니다. `return` 만나면 즉시 종료.

```python
def square(x):
    return x * x

n = square(5)   # 25
```

`return` 없으면 자동으로 `None` 반환.

## 4. 기본값 매개변수

호출 시 인수 생략하면 기본값 사용.

```python
def greet(name, greeting="안녕"):
    return f"{greeting}, {name}님!"

print(greet("길동"))                # 안녕, 길동님!
print(greet("Alice", "Hello"))     # Hello, Alice님!
```

## 5. 키워드 인수

순서 대신 이름으로 전달.

```python
def make_user(name, age, city):
    return {"name": name, "age": age, "city": city}

# 위치 인수
u1 = make_user("홍길동", 20, "서울")

# 키워드 인수 (순서 무관, 가독성 좋음)
u2 = make_user(city="부산", name="김영희", age=25)
```

## 6. 여러 값 반환 (튜플)

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)   # 1 5
```

## 7. 변수 스코프

함수 안에서 만든 변수는 **지역 변수** — 밖에서 안 보임.

```python
def f():
    x = 10        # 지역
    print(x)

f()
# print(x)        # NameError
```

함수 안에서 전역 변수를 **수정**하려면 `global` 키워드:
```python
total = 0
def add(n):
    global total
    total += n
```

(가능하면 `global` 은 피하고, 함수가 값을 받아서 반환하는 형태 권장.)

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_basic_function.py` | 정의·호출 |
| `02_default_args.py` | 기본값 매개변수 |
| `03_return.py` | return / 여러 값 반환 |
| `04_scope.py` | 지역/전역 변수 |

## ⚠️ 자주 하는 실수

1. **함수 호출에 `()` 빠뜨림**
   ```python
   def hi():
       print("hi")
   hi    # 함수 객체. 실행 안 됨
   hi()  # 실행
   ```

2. **`return` 없는데 결과 사용**
   ```python
   def show(x):
       print(x)
   y = show(5)   # y = None
   ```

3. **기본값에 가변 객체**
   ```python
   def add_to(item, lst=[]):    # ⚠️ 함정!
       lst.append(item)
       return lst
   add_to(1)   # [1]
   add_to(2)   # [1, 2] — 같은 리스트가 공유됨
   ```
   → 기본값은 `None` 으로 두고 함수 안에서 새로 생성:
   ```python
   def add_to(item, lst=None):
       if lst is None:
           lst = []
       ...
   ```

4. **이름 충돌**
   ```python
   def list():        # 내장 list 가려짐
       ...
   ```
   → `print`, `list`, `sum` 같은 내장 이름은 변수·함수명으로 쓰지 말 것.

## ❓ FAQ

**Q1. 함수는 몇 줄이 적절한가요?**
A. 권장 5~30줄. 너무 길면 더 작은 함수로 분리.

**Q2. `print` 와 `return` 의 차이?**
A. `print` 는 **화면에 출력**, `return` 은 **값을 반환**. 함수가 값 자체가 필요할 때는 return.

**Q3. 함수 안에서 함수를 호출할 수 있나요?**
A. 네. 자신을 호출(재귀)도 가능 (중급에서 다룸).

## 📝 과제 (exercises/)

- `exercise1.md` — 계산기 함수 모음
- `exercise2.md` — 입력 검증 함수 (`is_valid_age`)
- `exercise3.md` — 소수 판별 함수 (`is_prime`)

## 다음 주차

[10주차. 종합 실습](../week10_종합실습/) — 미니 프로젝트
