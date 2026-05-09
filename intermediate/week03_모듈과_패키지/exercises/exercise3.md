# 과제 3. `__name__ == "__main__"` 패턴

## 목표
모듈을 라이브러리로도, 스크립트로도 쓸 수 있게 만든다.

## 요구사항
- `greet.py` 작성
- `def greet(name)` 함수 정의
- `if __name__ == "__main__":` 안에서 사용자 입력 받아 인사 출력
- 다른 파일에서 `from greet import greet` 도 가능해야 함

## 검증
- `python greet.py` → 입력받아 인사 출력
- `python -c "from greet import greet; print(greet('Bob'))"` → 함수만 사용 (사용자 입력 없음)
