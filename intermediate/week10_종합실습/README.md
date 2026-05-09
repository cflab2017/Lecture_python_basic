# 10주차. 중급 종합 실습

> 단계: 중급 | 선수: 1~9주차 전부

## 학습 목표
- OOP·예외·파일 I/O를 모두 사용해 미니 프로젝트를 완성한다
- 모듈 분리와 패키지 구조를 적용한다

## 1. 프로젝트 설계 시 고려사항

1. **데이터 모델** — 어떤 클래스들로 표현?
2. **영구 저장** — JSON? CSV? 어떤 형태?
3. **사용자 인터페이스** — 명령어 형태? 메뉴 형태?
4. **모듈 분리** — `models.py`, `storage.py`, `cli.py` 등

## 2. 권장 패키지 구조

```
my_app/
├── __init__.py
├── models.py       # 클래스 정의 (Word, Book 등)
├── storage.py      # JSON 저장/로드
├── cli.py          # 메인 루프, 명령어 처리
└── main.py         # 진입점
```

## 3. 골격 예제 — 단어장 앱

`examples/wordbook_skeleton/` 참고.

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `wordbook_skeleton/models.py` | Word, WordBook 클래스 |
| `wordbook_skeleton/main.py` | 진입점 |

## ⚠️ 자주 하는 실수

1. **모든 코드를 `main.py` 한 파일에** — 분리 안 하면 200줄 넘어가면 미궁
2. **JSON 직렬화 안 되는 객체** — `dataclass` + `asdict()` 활용
3. **저장 시점이 잘못됨** — 매 변경 시 vs 종료 시 — 정책 정하기
4. **예외를 너무 좁게 또는 너무 넓게** — 회복 가능한 곳에서만 except

## ❓ FAQ

**Q1. dataclass 를 써도 되나요?**
A. 권장. 단순 데이터 클래스는 dataclass 가 편함. (고급 1주차에서 자세히)

**Q2. 단일 파일 vs 패키지?**
A. 단일 파일은 50줄 이하만. 그 이상이면 분리.

## 📝 최종 과제 (exercises/)

다음 4개 중 1개 선택.

1. `exercise1.md` — **단어장 앱** (CRUD + JSON + 퀴즈 모드)
2. `exercise2.md` — **간이 가계부** (수입/지출 + JSON + 카테고리)
3. `exercise3.md` — **로그 분석기** (정규식으로 분리 + CSV 리포트)
4. `exercise4.md` — **연락처 관리자 (OOP)** (Contact, AddressBook 클래스)

## 제출물
- 모듈 분리된 패키지 구조
- 예외 처리, 사용자 친화적 메시지
- README.md (실행법, 사용법)

## 다음 단계

중급 과정을 마쳤습니다! 🎉

- **고급 과정**: [../../advanced/](../../advanced/) — 타입 힌트, 데코레이터, 동시성, 테스트
- **실습 도전**: [../../practice/lv3_중급종합/](../../practice/lv3_중급종합/) (가계부, 도서 관리, 일기장, 텍스트 어드벤처)
