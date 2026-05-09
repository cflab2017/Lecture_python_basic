# 1주차. 함수 심화

> 단계: 중급 | 선수: 기초 9주차 (함수 기초)

## 학습 목표
- `*args`, `**kwargs` 로 가변 인자를 받는다
- 람다(lambda) 함수를 사용한다
- 고차함수 (`map`, `filter`, `sorted` with key) 를 활용한다
- 클로저(closure)의 동작을 이해한다

## 1. *args, **kwargs

가변 개수의 인자.

```python
def add_all(*args):           # args는 튜플
    return sum(args)

print(add_all(1, 2, 3))       # 6
print(add_all(1, 2, 3, 4, 5)) # 15

def info(**kwargs):           # kwargs는 딕셔너리
    for k, v in kwargs.items():
        print(f"{k}: {v}")

info(name="홍길동", age=20)
```

조합도 가능:
```python
def f(a, b, *args, **kwargs):
    ...
```

## 2. 람다 함수

이름 없는 한 줄 함수. 즉석 사용에 적합.

```python
square = lambda x: x * x
print(square(5))   # 25

# 보통 다른 함수의 인자로 전달
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, nums)))  # [2, 4, 6, 8, 10]
```

## 3. 고차함수

함수를 인자로 받는 함수.

```python
nums = [1, 2, 3, 4, 5]

# map: 변환
print(list(map(lambda x: x * x, nums)))      # [1, 4, 9, 16, 25]

# filter: 필터링
print(list(filter(lambda x: x % 2, nums)))   # [1, 3, 5]

# sorted with key
people = [("Alice", 30), ("Bob", 25), ("Charlie", 28)]
people.sort(key=lambda p: p[1])
print(people)
```

## 4. 클로저

함수 안에서 정의된 함수가 바깥 변수를 기억.

```python
def make_counter():
    count = 0
    def inc():
        nonlocal count    # 바깥 변수 수정 시 nonlocal 필요
        count += 1
        return count
    return inc

c = make_counter()
print(c(), c(), c())   # 1 2 3
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_args_kwargs.py` | 가변 인자 |
| `02_lambda.py` | 람다 함수 |
| `03_higher_order.py` | map / filter / sorted |
| `04_closure.py` | 클로저와 nonlocal |

## ⚠️ 자주 하는 실수

1. **`*args` 의 위치** — 일반 매개변수 뒤, `**kwargs` 앞.
2. **람다에 너무 많은 로직** — 길어지면 그냥 `def`. 람다는 한 줄.
3. **`sorted` 와 `sort` 혼동** — `sorted()` 는 새 리스트, `list.sort()` 는 제자리.
4. **클로저에서 `nonlocal` 누락** — `count += 1` 만 쓰면 UnboundLocalError.

## ❓ FAQ

**Q1. 언제 `*args` 를 써야 하나요?**
A. 인자 개수가 정해지지 않을 때. 예: `print`, `max(1, 2, 3, ...)`.

**Q2. 람다와 일반 함수의 성능 차이?**
A. 거의 없음. 람다는 가독성·간결함을 위한 문법 설탕.

**Q3. 클로저는 어디에 쓰나요?**
A. 데코레이터, 콜백, 상태가 있는 함수. 객체 대신 가벼운 대안.

## 📝 과제 (exercises/)

- `exercise1.md` — `stats(*nums)` 평균/분산
- `exercise2.md` — 학생 점수 정렬 (sorted with key)
- `exercise3.md` — `make_counter` 호출 카운터

## 다음 주차

[2주차. 컴프리헨션과 제너레이터](../week02_컴프리헨션과_제너레이터/) — 간결한 반복 표현
