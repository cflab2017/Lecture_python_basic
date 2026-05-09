"""BeautifulSoup 기본 — pip install beautifulsoup4"""
from bs4 import BeautifulSoup

html = """
<html><body>
    <h1>제목</h1>
    <ul>
        <li class="item">사과</li>
        <li class="item special">바나나</li>
        <li class="item">포도</li>
    </ul>
    <a href="/about">소개</a>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")

# 태그
print(soup.h1.text)
print(soup.find("a")["href"])

# find_all
items = soup.find_all("li")
for li in items:
    print("-", li.text, li.get("class"))

# CSS 선택자 (강력)
print([li.text for li in soup.select("li.item")])
print([li.text for li in soup.select("li.special")])
