"""헤드라인 스크래핑 — 동작 확인용 (HN)"""
import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (study)"}

r = requests.get(URL, headers=HEADERS, timeout=10)
r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")

titles = [a.get_text() for a in soup.select(".titleline > a")][:10]
for i, t in enumerate(titles, 1):
    print(f"{i}. {t}")
