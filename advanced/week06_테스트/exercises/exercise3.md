# 과제 3. mock으로 API 호출 테스트

## 목표
외부 API를 호출하는 함수를 mock 으로 테스트.

## 함수 예시
```python
def get_weather(city):
    import requests
    r = requests.get(f"https://api.example.com/weather?city={city}")
    if r.status_code == 200:
        return r.json()
    return None
```

## 테스트해야 할 시나리오
- 정상 응답 (200, JSON)
- 404 응답 → None
- 네트워크 에러 (예외)

`patch("requests.get")` 활용.
