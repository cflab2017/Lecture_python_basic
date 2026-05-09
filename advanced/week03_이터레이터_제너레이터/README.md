# 3주차. 이터레이터·제너레이터 심화

> 단계: 고급 | 선수: 2주차 + 중급 2주차

## 학습 목표
- 이터레이터 프로토콜 (`__iter__`, `__next__`) 을 직접 구현한다
- `yield from` 으로 제너레이터를 위임한다
- `itertools` 의 강력한 함수들을 활용한다
- 코루틴 기초 (`send`)

## 1. 이터레이터 프로토콜

`for ... in x` 는 사실 `iter(x)` → `next(it)` 반복.

```python
class Range:
    def __init__(self, start, stop):
        self.cur = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= self.stop:
            raise StopIteration
        self.cur += 1
        return self.cur - 1

print(list(Range(1, 5)))   # [1, 2, 3, 4]
```

## 2. yield from

다른 이터러블을 그대로 yield. 평탄화에 유용.

```python
def chain(*iters):
    for it in iters:
        yield from it

print(list(chain([1, 2], (3, 4), "ab")))   # [1, 2, 3, 4, 'a', 'b']
```

## 3. itertools

표준 라이브러리의 보석.

```python
import itertools as it

# 무한 시퀀스
counter = it.count(1, 2)        # 1, 3, 5, 7, ...
print(list(it.islice(counter, 5)))  # [1, 3, 5, 7, 9]

# 조합/순열
print(list(it.combinations([1, 2, 3, 4], 2)))   # (1,2),(1,3),(1,4),(2,3)...
print(list(it.permutations([1, 2, 3], 2)))

# 그룹
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
for key, group in it.groupby(data, key=lambda x: x[0]):
    print(key, list(group))

# 사전 곱
print(list(it.product([1, 2], "ab")))   # (1,'a'),(1,'b'),(2,'a'),(2,'b')

# 누적
print(list(it.accumulate([1, 2, 3, 4])))   # [1, 3, 6, 10]
```

## 4. 코루틴 기초

`yield` 가 양방향 통신 — `send(값)` 으로 값 주입.

```python
def echo():
    while True:
        x = yield
        print(f"받음: {x}")

co = echo()
next(co)            # 첫 yield까지 진행 (필수)
co.send("hello")    # 받음: hello
co.send("world")    # 받음: world
```

(파이썬 3.5+ 부터는 `async/await` 가 더 일반적 — 다음 주차)

## 5. 제너레이터 vs 리스트

| | 제너레이터 | 리스트 |
|---|------------|--------|
| 메모리 | 항목 1개씩 | 전체 |
| 길이 | 모름 | `len()` |
| 재사용 | 한 번만 | 여러 번 |
| 인덱싱 | 안 됨 | 됨 |

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_iterator.py` | 직접 이터레이터 구현 |
| `02_yield_from.py` | yield from |
| `03_itertools.py` | combinations, groupby, accumulate |
| `04_coroutine.py` | send 기반 코루틴 |

## ⚠️ 자주 하는 실수

1. **이터레이터를 두 번 순회** — 두 번째는 빈 결과. 다시 생성 필요.
2. **`__next__` 에서 StopIteration 누락** — 무한 루프.
3. **groupby 전 정렬 안 함** — groupby는 연속된 같은 키만 묶음.

## ❓ FAQ

**Q1. 이터레이터와 제너레이터의 차이?**
A. 제너레이터는 이터레이터의 한 종류. yield 로 만든 것.

**Q2. `itertools` 보다 `more-itertools` 가 더 좋다는데?**
A. 표준은 아니지만 강력. 실무에서 자주 사용.

## 📝 과제 (exercises/)

- `exercise1.md` — `chunked_lines(path, n)` 제너레이터
- `exercise2.md` — `groupby` 로 로그 날짜별 그룹
- `exercise3.md` — 무한 피보나치 + islice

## 다음 주차

[4주차. 동시성 (1) - threading](../week04_동시성_threading/)
