# 2주차. 데코레이터와 컨텍스트 매니저

> 단계: 고급 | 선수: 1주차

## 학습 목표
- 함수 데코레이터를 정의하고 적용한다
- 인자 받는 데코레이터를 만든다
- 클래스/함수 기반 컨텍스트 매니저를 구현한다
- `@functools.wraps` 의 역할을 안다

## 1. 데코레이터란

함수를 인자로 받아 새로운 함수를 반환. **기능을 횡단으로 추가** (로깅, 캐싱, 인증 등).

```python
def loud(func):
    def wrapper(*args, **kwargs):
        print(f">>> {func.__name__} 호출")
        result = func(*args, **kwargs)
        print(f"<<< 결과: {result}")
        return result
    return wrapper

@loud
def add(a, b):
    return a + b

add(3, 5)
# >>> add 호출
# <<< 결과: 8
```

`@loud` 는 `add = loud(add)` 의 문법 설탕.

## 2. functools.wraps

데코레이터로 감싸도 원본 함수 이름·docstring 유지.

```python
from functools import wraps

def loud(func):
    @wraps(func)            # 이거 없으면 .__name__ 이 'wrapper' 됨
    def wrapper(*args, **kwargs):
        ...
    return wrapper
```

## 3. 인자 받는 데코레이터

데코레이터를 만드는 함수 (3중 함수).

```python
def retry(times):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"재시도 {i+1}/{times}: {e}")
            raise
        return wrapper
    return deco

@retry(3)
def fragile():
    ...
```

## 4. 컨텍스트 매니저

`with` 문에서 동작. 자원 획득·해제를 안전하게.

### 클래스 기반
```python
class FileLock:
    def __init__(self, path):
        self.path = path
    def __enter__(self):
        print(f"잠금: {self.path}")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("해제")

with FileLock("data.txt"):
    print("작업 중")
```

### 함수 기반 (`contextmanager`)
```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label):
    start = time.perf_counter()
    yield                   # 여기서 with 블록 실행됨
    print(f"{label}: {time.perf_counter() - start:.4f}s")

with timer("작업"):
    sum(range(1_000_000))
```

## 5. 실전 — 메모이제이션

```python
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

fib(100)   # 빠름
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_basic_decorator.py` | 함수 데코레이터 + wraps |
| `02_param_decorator.py` | 인자 받는 데코레이터 (retry) |
| `03_context_class.py` | 클래스 기반 컨텍스트 매니저 |
| `04_contextmanager.py` | `@contextmanager` 함수 기반 |

## ⚠️ 자주 하는 실수

1. **`@wraps` 누락** — 디버깅·문서가 망가짐. 항상 붙이기.
2. **데코레이터가 `return` 안 함** — 결과가 None.
3. **`@contextmanager` 함수 안에서 yield 가 두 개 이상** — 한 번만.
4. **컨텍스트 매니저의 예외 무시** — `__exit__` 가 True 반환하면 예외 삼킴.

## ❓ FAQ

**Q1. 데코레이터는 언제 쓰나요?**
A. 여러 함수에 같은 부가 동작 (로깅, 인증, 캐싱) 을 넣을 때.

**Q2. `with` 와 `try-finally` 의 차이?**
A. `with` 는 정형화된 `try-finally`. 가독성·실수 방지.

**Q3. 데코레이터를 여러 개 쌓으면?**
A. 아래쪽이 먼저 적용. `@A @B def f()` → `f = A(B(f))`.

## 📝 과제 (exercises/)

- `exercise1.md` — `@logged` 함수 호출 로깅
- `exercise2.md` — `@cached` 메모이제이션
- `exercise3.md` — `with timer("...")` 컨텍스트 매니저

## 다음 주차

[3주차. 이터레이터·제너레이터 심화](../week03_이터레이터_제너레이터/)
