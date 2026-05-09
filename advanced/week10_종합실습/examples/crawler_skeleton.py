"""비동기 크롤러 + Pandas 분석 골격"""
import asyncio
import httpx
import pandas as pd
from dataclasses import dataclass

@dataclass
class Article:
    title: str
    score: int
    url: str

async def fetch_one(client: httpx.AsyncClient, url: str) -> str:
    r = await client.get(url, timeout=10)
    return r.text

async def fetch_articles() -> list[Article]:
    """실제로는 BeautifulSoup으로 파싱.
    여기는 더미 데이터 반환."""
    async with httpx.AsyncClient() as client:
        urls = [f"https://httpbin.org/uuid" for _ in range(5)]
        results = await asyncio.gather(*[fetch_one(client, u) for u in urls])
    return [
        Article(title=f"Article {i}", score=100 - i * 10, url=u)
        for i, u in enumerate(urls)
    ]

async def main():
    articles = await fetch_articles()
    df = pd.DataFrame([a.__dict__ for a in articles])
    print(df)
    print(f"\n평균 점수: {df.score.mean()}")
    df.to_csv("articles.csv", index=False)

if __name__ == "__main__":
    asyncio.run(main())
