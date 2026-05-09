# 과제 15. 콘솔 챗봇

> 난이도: Lv ★★★★ | 사전지식: 고급 7주차 (requests)

## 목표
콘솔 기반 챗봇 (규칙 또는 LLM API)

## 요구사항
- 사용자 입력 ↔ 응답 반복
- 종료 명령(`/quit`, `/exit`)
- 대화 이력 JSON 저장
- 명령어 모드: `/clear`, `/save`, `/load`, `/history`

## 선택 옵션
- A. **규칙 기반**: 키워드 매칭
- B. **API 기반**: requests 로 LLM API + .env (`python-dotenv`)

## 도전 과제
- 토큰 사용량
- 비동기 다중 모델
