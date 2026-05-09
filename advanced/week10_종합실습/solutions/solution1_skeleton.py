"""최종 과제 1 해답 골격 — 비동기 크롤러 + Pandas

실제 동작은 의존성 설치(httpx, pandas, beautifulsoup4) 후.
"""
import asyncio
import json
from dataclasses import dataclass, asdict

@dataclass
class Article:
    title: str
    score: int
    url: str

async def fetch_articles() -> list[Article]:
    # TODO: 실제 사이트 파싱
    return [
        Article(title=f"기사{i}", score=100 - i * 5, url=f"https://example.com/{i}")
        for i in range(20)
    ]

def analyze(articles: list[Article]) -> dict:
    if not articles:
        return {}
    scores = [a.score for a in articles]
    return {
        "count": len(articles),
        "avg": sum(scores) / len(scores),
        "max": max(scores),
        "min": min(scores),
    }

async def main():
    articles = await fetch_articles()
    stats = analyze(articles)
    print(json.dumps(stats, indent=2))

    # CSV 저장
    with open("articles.csv", "w", encoding="utf-8") as f:
        f.write("title,score,url\n")
        for a in articles:
            f.write(f"{a.title},{a.score},{a.url}\n")

if __name__ == "__main__":
    asyncio.run(main())
