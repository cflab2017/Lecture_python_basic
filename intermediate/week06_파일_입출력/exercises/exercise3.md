# 과제 3. To-Do JSON 영구 저장

## 목표
기초 10주차의 To-Do List 프로그램에 JSON 저장을 추가한다.

## 요구사항
- 시작 시 `todos.json` 이 있으면 로드
- 매번 변경 후 저장 (또는 종료 시 한 번에)
- 종료 후 다시 실행해도 데이터 유지

## 데이터 구조
```json
[
  {"task": "우유 사기", "done": false},
  {"task": "책 읽기", "done": true}
]
```
