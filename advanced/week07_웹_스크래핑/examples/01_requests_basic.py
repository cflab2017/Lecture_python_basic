"""requests 기본 — pip install requests 필요"""
import requests

# JSON API 호출
r = requests.get("https://httpbin.org/json", timeout=10)
print(r.status_code)
print(r.json())

# GET with params
r = requests.get("https://httpbin.org/get",
    params={"q": "python", "lang": "ko"},
    timeout=10)
print(r.url)
print(r.json()["args"])

# POST
r = requests.post("https://httpbin.org/post",
    data={"key": "value"},
    timeout=10)
print(r.json()["form"])
