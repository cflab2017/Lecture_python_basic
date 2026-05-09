# 과제 2. 사용자 정의 예외 InvalidScoreError

## 목표
점수가 0~100 범위가 아니면 발생하는 예외를 만든다.

## 요구사항
- `class InvalidScoreError(Exception): ...`
- `validate_score(s)` 함수: 0~100 외면 `InvalidScoreError` 발생
- main: 점수 입력 → 검증 → 정상이면 학점 출력
