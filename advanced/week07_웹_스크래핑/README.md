# 7주차. 웹 스크래핑

> 단계: 고급 | 선수: 6주차

## 학습 목표
- `requests` 로 HTTP 요청
- `BeautifulSoup` 으로 HTML 파싱
- 헤더·세션·쿠키 다루기
- robots.txt 와 매너

## 1. requests

```python
import requests

r = requests.get("https://example.com")
print(r.status_code)        # 200
print(r.text[:200])         # HTML 일부
print(r.headers["Content-Type"])

# JSON API
r = requests.get("https://api.github.com/users/python")
data = r.json()
print(data["public_repos"])
```

## 2. POST 요청

```python
r = requests.post("https://httpbin.org/post",
    data={"key": "value"},
    headers={"User-Agent": "MyBot 1.0"},
)
```

## 3. BeautifulSoup

```bash
pip install beautifulsoup4 lxml
```

```python
from bs4 import BeautifulSoup

html = """<html><body>
    <h1>제목</h1>
    <ul>
        <li class="item">A</li>
        <li class="item">B</li>
    </ul>
</body></html>"""

soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text)
print(soup.find("h1").text)
print([li.text for li in soup.find_all("li")])
print([li.text for li in soup.select("li.item")])   # CSS 선택자
```

## 4. 세션과 쿠키

```python
session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"})

# 로그인
session.post("https://example.com/login", data={"user": "x", "pass": "y"})

# 같은 세션으로 요청 → 쿠키 유지
r = session.get("https://example.com/me")
```

## 5. 매너와 윤리

- **robots.txt 확인**: `https://example.com/robots.txt`
- **요청 간격**: `time.sleep(1)` 정도 권장
- **사용자 에이전트**: 정직하게 표시
- **저작권·약관 준수**

## 6. 실전 패턴

```python
import requests
from bs4 import BeautifulSoup
import time

URL = "https://news.ycombinator.com"
HEADERS = {"User-Agent": "Mozilla/5.0 (study)"}

def fetch_titles():
    r = requests.get(URL, headers=HEADERS, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    titles = [a.get_text() for a in soup.select(".titleline > a")]
    return titles[:10]

for i, title in enumerate(fetch_titles(), 1):
    print(f"{i}. {title}")
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_requests_basic.py` | GET, JSON |
| `02_bs4_parse.py` | HTML 파싱 |
| `03_session.py` | 세션 + 쿠키 |
| `04_scrape_demo.py` | 실제 스크래핑 (httpbin) |

## ⚠️ 자주 하는 실수

1. **timeout 누락** — 무한 대기 위험. 항상 `timeout=10` 정도.
2. **`r.raise_for_status()` 안 함** — 404를 못 알아챔.
3. **HTML 파서 미지정** — 명시적으로 `"html.parser"` 또는 `"lxml"`.
4. **선택자 너무 깨지기 쉬움** — id/class가 자주 바뀜. 견고한 선택자 사용.
5. **차단당함** — 너무 빠른 요청. `time.sleep` 으로 간격.

## ❓ FAQ

**Q1. JavaScript 가 렌더링하는 페이지는?**
A. requests로 안 됨. Selenium 또는 Playwright 사용.

**Q2. 동적 사이트는?**
A. 보통 내부 API를 직접 호출 (개발자 도구 → 네트워크 탭에서 발견).

**Q3. 로그인 후 페이지를 가져오려면?**
A. Session 사용. CSRF 토큰까지 다뤄야 할 수도.

## 📝 과제 (exercises/)

- `exercise1.md` — 뉴스 헤드라인 Top 10
- `exercise2.md` — GitHub 사용자 저장소 정보
- `exercise3.md` — robots.txt 확인 함수

## 다음 주차

[8주차. NumPy / Pandas](../week08_NumPy_Pandas/)
