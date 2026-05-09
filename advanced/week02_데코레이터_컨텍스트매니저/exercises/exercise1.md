# 과제 1. @logged 함수 호출 로깅

## 목표
함수 호출을 파일에 로깅하는 데코레이터.

## 요구사항
- 호출 시 함수명, 인자, 결과를 `app.log` 에 한 줄로 기록
- 형식: `2026-05-09 14:30 add(3, 5) -> 8`

## 사용 예
```python
@logged
def add(a, b):
    return a + b

add(3, 5)
# app.log 에 기록됨
```
