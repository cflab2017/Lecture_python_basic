# 2주차. 컴프리헨션과 제너레이터

> 단계: 중급 | 선수: 1주차 (함수 심화)

## 학습 목표
- 리스트·딕셔너리·집합 컴프리헨션을 작성한다
- 제너레이터 함수와 표현식을 이해한다
- 메모리 효율적인 코드를 짠다

## 1. 리스트 컴프리헨션

`[표현식 for 변수 in 시퀀스 if 조건]` 한 줄로 리스트 생성.

```python
# 기존
squares = []
for x in range(10):
    squares.append(x * x)

# 컴프리헨션
squares = [x * x for x in range(10)]
```

조건 추가:
```python
even_sq = [x * x for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

중첩:
```python
pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
```

## 2. 딕셔너리·집합 컴프리헨션

```python
words = ["apple", "banana", "cherry"]

# 딕셔너리: {키: 값 for ...}
length_map = {w: len(w) for w in words}
# {'apple': 5, 'banana': 6, 'cherry': 6}

# 집합: {표현식 for ...}
unique_lens = {len(w) for w in words}
# {5, 6}
```

## 3. 제너레이터 함수

`return` 대신 `yield`. 결과를 한 번에 만들지 않고, 필요할 때마다 하나씩.

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for x in fib(10):
    print(x, end=" ")    # 0 1 1 2 3 5 8 13 21 34
```

리스트로 한 번에 보고 싶으면 `list(fib(10))`.

## 4. 제너레이터 표현식

대괄호 대신 소괄호 → 메모리 절약.

```python
# 리스트 컴프리헨션 (메모리 다 잡아먹음)
total = sum([x * x for x in range(1_000_000)])

# 제너레이터 표현식 (한 번에 하나씩)
total = sum(x * x for x in range(1_000_000))
```

## 5. 언제 어느 것?

| 상황 | 도구 |
|------|------|
| 작은 데이터 + 인덱스 필요 | 리스트 컴프리헨션 |
| 큰 데이터 + 한 번 순회 | 제너레이터 |
| 키-값 매핑 | 딕셔너리 컴프리헨션 |
| 중복 제거 | 집합 컴프리헨션 |

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_list_comp.py` | 리스트 컴프리헨션 |
| `02_dict_set_comp.py` | 딕셔너리·집합 |
| `03_generator.py` | 제너레이터 함수 |
| `04_generator_expr.py` | 제너레이터 표현식 (메모리 비교) |

## ⚠️ 자주 하는 실수

1. **컴프리헨션이 너무 길고 복잡** — 가독성 떨어지면 그냥 for 루프
2. **제너레이터를 두 번 순회** — 한 번 다 돌면 빈 상태. 다시 호출 필요.
3. **`yield` 가 함수 어디에든 있으면 함수 전체가 제너레이터** — `return` 으로 일반 값 못 돌려줌

## ❓ FAQ

**Q1. 컴프리헨션이 for문보다 항상 빠른가요?**
A. 보통 약간 빠름. 가장 큰 차이는 가독성과 의도 표현.

**Q2. 제너레이터의 길이를 알 수 있나요?**
A. 안 됨. 길이가 필요하면 list로 변환 (메모리 사용).

**Q3. yield 가 여러 개여도 되나요?**
A. 네. 호출할 때마다 다음 yield 까지 실행됨.

## 📝 과제 (exercises/)

- `exercise1.md` — 1~100 소수 (컴프리헨션)
- `exercise2.md` — 단어 길이 매핑
- `exercise3.md` — 큰 파일 라인 단위 제너레이터

## 다음 주차

[3주차. 모듈과 패키지](../week03_모듈과_패키지/)
