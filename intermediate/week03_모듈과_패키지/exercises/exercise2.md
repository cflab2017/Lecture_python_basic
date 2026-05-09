# 과제 2. string_utils.py

## 목표
문자열 유틸리티 모듈 작성.

## 함수
- `slugify(text)` — 양쪽 공백 제거, 소문자, 공백을 `-` 로 치환
- `truncate(text, max_len)` — `max_len` 보다 길면 `...` 으로 줄임
- `wrap(text, width)` — `width` 마다 줄바꿈

## 사용 예
```python
print(slugify(" Hello World "))      # "hello-world"
print(truncate("이 문장은 길어요", 5)) # "이 문..."
print(wrap("abcdefghij", 4))          # "abcd\nefgh\nij"
```
