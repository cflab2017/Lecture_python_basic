# 최종 과제 1. 비동기 크롤러 + 분석

## 목표
관심 사이트의 데이터를 비동기로 수집 → Pandas 로 분석 → 리포트.

## 요구사항
- 데이터 소스: 뉴스/Hacker News/공공 API 등
- `httpx` 또는 `aiohttp` 비동기 fetch
- 수집 결과를 dataclass 로
- pandas 로 통계 (`describe()`, `groupby()`)
- 결과를 CSV + JSON 으로 저장
- pytest 테스트 (mock 사용)
