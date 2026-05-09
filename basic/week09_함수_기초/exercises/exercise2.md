# 과제 2. 입력 검증 함수

## 목표
`is_valid_age(value)` 함수를 만든다.

## 요구사항
- 입력값이 0~120 사이의 정수면 `True`, 아니면 `False`
- 문자열이 들어와도 처리 (예: `"abc"` → False)

## 입출력 예시 (테스트 코드 작성)
```python
print(is_valid_age(20))      # True
print(is_valid_age(0))       # True
print(is_valid_age(120))     # True
print(is_valid_age(-1))      # False
print(is_valid_age(150))     # False
print(is_valid_age("abc"))   # False
```
