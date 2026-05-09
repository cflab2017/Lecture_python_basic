# 10주차. 종합 실습

> 단계: 기초 | 선수: 1~9주차 전부

## 학습 목표
- 지금까지 배운 모든 내용을 합쳐 작은 프로그램을 완성한다
- 입력·조건·반복·자료구조·함수를 자연스럽게 조합한다
- 디버깅과 코드 정리 경험을 쌓는다

## 1. 프로젝트 설계 절차

1. **요구사항 정리** — 무엇을 만드는지, 어떤 입출력인지 종이에 적기
2. **데이터 구조 결정** — 리스트? 딕셔너리? 둘 다?
3. **함수 분리** — 작은 단위로 (입력 받기, 처리, 출력 등)
4. **흐름 작성** — main 루프, 종료 조건
5. **점진적으로 만들기** — 한 번에 다 짜지 말고, 한 기능씩 동작 확인

## 2. 디버깅 기초

### print 디버깅
가장 단순하고 강력한 방법.
```python
def calc(x, y):
    print(f"DEBUG: x={x}, y={y}")
    result = x / y
    print(f"DEBUG: result={result}")
    return result
```

### 에러 메시지 읽기
가장 아래의 한 줄이 핵심.
```
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    print(scores[5])
IndexError: list index out of range
```
→ "10번째 줄에서 리스트 인덱스 범위 초과"

## 3. 골격 예제 — 미니 To-Do List

`examples/todo_skeleton.py` 참고.

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `todo_skeleton.py` | To-Do List 골격 |
| `debug_demo.py` | print 디버깅 / try-except 맛보기 |

## ⚠️ 자주 하는 실수

1. **한꺼번에 모든 기능 구현 시도** — 작게 잘라서 단계별로
2. **함수 분리 없이 한 덩어리 코드** — 읽기 어렵고 디버깅 힘듦
3. **에러를 `try: ... except: pass` 로 숨김** — 어디서 뭐가 잘못됐는지 모름
4. **변수명을 `a`, `b`, `temp` 로** — 의미 있는 이름 (`scores`, `user_input`)

## ❓ FAQ

**Q1. 어디서부터 시작해야 할지 모르겠어요.**
A. "프로그램이 시작되면 무엇이 화면에 나오는가" → "사용자가 무엇을 입력하는가" → 그 흐름을 그대로 코드로.

**Q2. 막히면 어떻게 해요?**
A. 한 줄씩 print로 출력해서 데이터를 확인. 그래도 안 되면 검색 (StackOverflow). 그래도 안 되면 질문.

## 📝 최종 과제 (exercises/)

다음 4개 중 1개를 선택해서 완성도 있게 작성.

1. `exercise1.md` — **콘솔 To-Do List** (추가/조회/완료/삭제)
2. `exercise2.md` — **단어장 퀴즈** (영-한 매핑)
3. `exercise3.md` — **간이 가계부** (수입/지출/잔액)
4. `exercise4.md` — **숫자 야구 게임** (스트라이크/볼)

## 제출물
- `.py` 소스 파일
- 짧은 README (실행법, 사용한 문법)
- 시연 스크린샷 또는 녹화

## 다음 단계

기초 과정을 마쳤습니다! 🎉

- **중급 과정**: [../../intermediate/](../../intermediate/) — 함수 심화, OOP, 파일 I/O
- **실습 도전**: [../../practice/lv1_기초응용](../../practice/lv1_기초응용/), [../../practice/lv2_자료구조](../../practice/lv2_자료구조/)
