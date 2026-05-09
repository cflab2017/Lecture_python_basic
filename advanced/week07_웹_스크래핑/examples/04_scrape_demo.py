"""실제 스크래핑 데모 — httpbin 의 HTML 페이지 활용"""
import requests
from bs4 import BeautifulSoup

URL = "https://httpbin.org/html"
HEADERS = {"User-Agent": "Mozilla/5.0 (study)"}

r = requests.get(URL, headers=HEADERS, timeout=10)
r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")

print("=== 제목 ===")
print(soup.h1.text)

print("\n=== 본문 일부 ===")
p = soup.find("p")
if p:
    print(p.text[:200])
