# 과제 3. robots.txt 확인 함수

## 목표
특정 URL이 크롤링 허용되는지 robots.txt 로 검사하는 함수.

## 함수 시그니처
```python
def can_crawl(url: str, user_agent: str = "*") -> bool: ...
```

## 힌트
- `urllib.robotparser` 활용
- 또는 robots.txt 직접 파싱

## 사용 예
```python
print(can_crawl("https://example.com/page"))    # True
print(can_crawl("https://example.com/admin"))   # False (Disallow된 경로면)
```
