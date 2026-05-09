# 과제 3. with timer("...") 컨텍스트 매니저

## 목표
실행 시간을 측정하는 컨텍스트 매니저.

## 요구사항
- `@contextmanager` 또는 클래스 기반 둘 다 OK
- 예외 발생해도 시간 출력 (try/finally)
- 출력 형식: `[timer] 작업명: 0.1234s`

## 사용 예
```python
with timer("정렬"):
    sorted(big_list)

with timer("API 호출"):
    requests.get(...)
```
