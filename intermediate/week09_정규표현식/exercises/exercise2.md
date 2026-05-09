# 과제 2. 휴대폰 번호 검증

## 목표
함수 `is_valid_phone(s) -> bool` 작성.

## 형식
- `010-XXXX-XXXX` (X는 숫자)
- `010` 으로 시작
- 하이픈 필수

## 테스트 케이스
```python
assert is_valid_phone("010-1234-5678")
assert not is_valid_phone("011-1234-5678")
assert not is_valid_phone("010 1234 5678")
assert not is_valid_phone("010-12345-678")
```
