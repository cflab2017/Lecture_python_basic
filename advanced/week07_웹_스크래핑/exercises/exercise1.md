# 과제 1. 뉴스 헤드라인 Top 10

## 목표
임의의 뉴스 사이트(또는 Hacker News)에서 헤드라인 10개를 추출.

## 요구사항
- requests + BeautifulSoup
- timeout, raise_for_status, User-Agent 모두 설정
- 결과를 CSV 또는 화면에 출력

## 권장 사이트
- Hacker News: https://news.ycombinator.com (`.titleline > a`)
- 또는 RSS 피드 (정확한 형식)
