# 과제 5. To-Do List (확장판)

> 난이도: Lv ★★ | 사전지식: 기초 6-9주차

## 목표
할 일 추가/조회/완료/삭제 + 우선순위 + 마감일

## 기초 과제와의 차별점
- **기초 10주차 골격** = add/show/done 3개 명령
- **여기** = 5개 명령 + 우선순위 + 마감일 + 정렬·필터

## 요구사항
- 데이터: `[{"task": str, "done": bool, "priority": str, "due": str}, ...]`
- 명령: `add`, `list`, `done <번호>`, `del <번호>`, `quit`
- 우선순위 (높음/보통/낮음)
- `list --pending`, `list --sort priority`

## 도전 과제
- 마감 임박 강조
- 카테고리(태그)
