# 과제 1. 다중 URL 동시 다운로드

## 목표
URL 리스트를 받아 응답 크기를 출력. 순차 vs 스레드 시간 비교.

## 요구사항
- `requests` 사용
- 8~10개 URL (httpbin.org/delay/N 같은 거 활용 가능)
- 두 방식 모두 측정해서 시간 출력

## 도전
- `as_completed` 로 먼저 끝난 것부터 처리
