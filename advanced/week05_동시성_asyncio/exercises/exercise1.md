# 과제 1. 동시 fetch 시간 측정

## 목표
10개의 가짜 URL fetch를 동시 vs 순차로 실행. 시간 비교.

## 요구사항
- `asyncio.sleep(0.5)` 로 네트워크 시뮬레이션
- `asyncio.gather` 로 동시 실행
- 두 시간 출력 (이론상 5s vs 0.5s)

## 도전
- 실제 `httpx` 로 https://httpbin.org/delay/1 호출
