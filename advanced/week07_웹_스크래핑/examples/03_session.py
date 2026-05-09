"""Session 사용 — 같은 헤더/쿠키 유지"""
import requests

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (study)"})

# 첫 요청
r = session.get("https://httpbin.org/cookies/set?session_id=abc123")
print("쿠키 받음:", session.cookies.get_dict())

# 같은 세션의 다음 요청은 쿠키를 자동 전달
r = session.get("https://httpbin.org/cookies")
print("서버가 본 쿠키:", r.json())
