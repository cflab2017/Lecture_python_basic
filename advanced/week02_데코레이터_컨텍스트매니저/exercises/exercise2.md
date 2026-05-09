# 과제 2. @cached 메모이제이션

## 목표
함수 결과를 캐시해서 같은 인자로 재호출 시 빠르게.

## 요구사항
- 인자(튜플)를 키로 하는 dict 캐시
- `@wraps` 사용
- `cache_info()` — 적중/미스 카운트 (보너스)

## 사용 예
```python
@cached
def slow_square(n):
    time.sleep(0.5)
    return n * n

slow_square(5)   # 0.5초
slow_square(5)   # 즉시 (캐시 적중)
```
