# 파이썬 강의 - 실습과제 (CLI 프로젝트 모음)

> 본 과정은 **기초 / 중급 / 고급 / 실습과제** 4단계 커리큘럼 중 **4단계 (실습과제)** 입니다.
> 모든 과제는 **CLI(Command Line Interface)** 기반으로, 터미널에서 실행되는 콘솔 프로그램입니다.

## 과정 개요

- **목적**: 기초~고급에서 배운 문법·자료구조·OOP·라이브러리를 **하나의 동작하는 프로그램**으로 통합
- **구성**: 난이도 4단계 × 과제 4개 = **총 16개 CLI 프로젝트**
- **각 과제 형식**: 목표 → 필요 사전지식 → (기초 과제와의 차별점) → 요구사항 → 입출력 예시 → 핵심 코드 힌트 → 도전 과제
- **권장 진행 속도**: 주당 1~2개

## 과제 난이도 표

| Lv | 단계 | 사전 지식 | 대표 과제 |
|----|------|-----------|----------|
| ★ | 기초 응용 | 기초 1~5주차 (변수·조건문·반복문·함수) | 가위바위보, 숫자 맞추기 |
| ★★ | 자료구조 활용 | 기초 6~9주차 (리스트·딕셔너리·문자열·함수) | To-Do List, 단어장 퀴즈 |
| ★★★ | 중급 종합 | 중급 5~8주차 (예외·파일·OOP) | 가계부, 도서 관리, 일기장 |
| ★★★★ | 고급 응용 | 고급 1~7주차 (타입힌트·데코레이터·외부 라이브러리) | argparse CLI, CSV 분석, TUI 앱 |

> **중요**: Lv ★~★★ 과제는 기초 과정의 주차별 과제와 주제가 겹치는 경우가 있습니다.
> 실습과제 버전은 **난이도가 한 단계 상향**된 확장 버전으로, 기능과 요구사항이 더 많습니다.

---

## Lv ★ — 기초 응용

### 과제 1. 가위바위보 (확장판)

**목표**: 사용자 vs 컴퓨터 가위바위보 — 3판 2선승, 통산 전적 누적

**필요 사전지식**: 기초 4주차(조건문) + 5주차(반복문) + `random` 모듈

**기초 과제와의 차별점**
- 기초 4주차의 가위바위보 = **1회 결과 출력 후 종료**
- 실습 1번 = **3판 2선승 + 무한 루프 + 잘못된 입력 재요청 + 통산 전적 누적**

**요구사항**
- 사용자 입력: `가위`, `바위`, `보` (한글 또는 `r/p/s`)
- 컴퓨터는 `random.choice`로 선택
- 매 라운드마다 결과 출력 (승/패/무)
- 3승 먼저 달성한 쪽이 최종 승자
- 잘못된 입력 시 재요청

**입출력 예시**
```
[1라운드] 선택(가위/바위/보): 가위
컴퓨터: 보  → 사용자 승!  (1 : 0)
[2라운드] 선택(가위/바위/보): 바위
컴퓨터: 바위 → 무승부      (1 : 0)
...
최종 승자: 사용자
한 게임 더? (y/n): y
```

**핵심 코드 힌트**
```python
import random

CHOICES = ["가위", "바위", "보"]

def judge(user, com):
    if user == com:
        return "무"
    win = {"가위": "보", "바위": "가위", "보": "바위"}
    return "승" if win[user] == com else "패"
```

**도전 과제**
- 통산 전적(승/패/무 횟수)을 세션 동안 누적
- 컴퓨터 AI: 사용자 패턴 학습해서 다음 수 예측

---

### 과제 2. 숫자 맞추기 (확장판)

**목표**: 1~100 사이 랜덤 숫자를 사용자가 맞히기 — 시도 제한 + 난이도 선택

**필요 사전지식**: 기초 4주차(조건문) + 5주차(반복문) + 9주차(함수)

**기초 과제와의 차별점**
- 기초 5주차의 숫자 맞추기 = **단순 더 큼/작음 비교 + 시도 횟수**
- 실습 2번 = **시도 제한 + 난이도 선택 + 재도전 옵션 + 함수 분리**

**요구사항**
- 시작 시 난이도 선택 (쉬움 1~50 / 보통 1~100 / 어려움 1~500)
- 시도 제한 (예: 7회) — 초과 시 정답 공개
- 매 시도마다 "더 큰/작은 수" 힌트 + 남은 횟수
- 함수 분리: `play_round()`, `pick_difficulty()`

**입출력 예시**
```
난이도(1.쉬움 2.보통 3.어려움): 2
1~100 사이 숫자를 7번 안에 맞춰보세요.
[남은 7회] 숫자: 50  → 더 큰 수입니다.
[남은 6회] 숫자: 75  → 더 작은 수입니다.
[남은 5회] 숫자: 63  → 정답! (시도 3회)
```

**도전 과제**
- 베스트 기록 파일에 저장
- 사용자가 정답을 정하고 컴퓨터가 맞히는 모드

---

### 과제 3. CLI 계산기

**목표**: 메뉴 선택형 사칙연산 계산기 — 결과 누적 사용 가능

**필요 사전지식**: 기초 4주차(조건문) + 9주차(함수)

**기초 과제와의 차별점**
- 기초 9주차 = **`add/sub/mul/div` 함수 정의 + 메뉴 선택**
- 실습 3번 = **결과 누적(이전 결과를 다음 연산에 사용) + 이력 저장 + 0 나누기 처리**

**요구사항**
- 메뉴: 1.+ 2.- 3.× 4.÷ 5.이전 결과 사용 6.종료
- 0으로 나누기 예외 처리 (메시지 출력 후 메뉴로)
- 종료 시 전체 연산 이력 출력

**입출력 예시**
```
[메뉴] 1.+ 2.- 3.* 4./ 5.이전 결과 6.종료
선택: 1
첫 번째 수: 10
두 번째 수: 5
결과: 15  (이전 결과로 저장)
```

**도전 과제**
- 제곱(`**`), 나머지(`%`), 절댓값 추가
- `eval` 없이 수식 문자열 파싱 (`3 + 4 * 2`)

---

### 과제 4. 단위 변환기

**목표**: 길이/무게/온도/환율 변환 CLI

**필요 사전지식**: 기초 3주차(연산자·입출력) + 9주차(함수)

**기초 과제와의 차별점**
- 기초 2주차 = **단방향 단일 변환** (예: cm → inch)
- 실습 4번 = **메뉴형 + 양방향 변환 + 다중 카테고리 + 모듈 분리**

**요구사항**
- 카테고리 선택 → 변환 방향 선택 → 입력값 → 결과
- 카테고리: 길이(cm↔inch, m↔ft) / 무게(kg↔lb) / 온도(°C↔°F) / 환율(KRW↔USD)
- 변환 함수는 `converter.py` 모듈로 분리
- 소수점 둘째 자리까지 출력

**도전 과제**
- 환율은 외부 API에서 실시간 조회
- 단위를 자유 입력 (`5 km to mile`)

---

## Lv ★★ — 자료구조 활용

### 과제 5. To-Do List (확장판)

**목표**: 할 일 추가/조회/완료/삭제 + 우선순위 + 마감일

**필요 사전지식**: 기초 6주차(리스트) + 7주차(딕셔너리) + 9주차(함수)

**기초 과제와의 차별점**
- 기초 10주차 골격 = **add/show/done 3개 명령**
- 실습 5번 = **add/list/done/del/edit 5개 명령 + 우선순위 + 마감일 + 정렬**

**요구사항**
- 데이터: `[{"task": str, "done": bool, "priority": str, "due": str}, ...]`
- 명령: `add`, `list`, `done <번호>`, `del <번호>`, `edit <번호>`, `quit`
- 우선순위(높음/보통/낮음)별 색상/마커
- `list --sort priority` 정렬 옵션
- `list --pending` 미완료만

**입출력 예시**
```
> add 우유 사기 --priority high --due 2026-05-15
추가됨 #1: [높음] 우유 사기 (~05-15)
> list --pending
1. [ ][높음] 우유 사기 (~05-15)
2. [ ][보통] 책 반납 (~05-20)
> done 1
완료: 우유 사기
```

**핵심 코드 힌트**
```python
todos = []

def add(task, priority="보통", due=None):
    todos.append({"task": task, "done": False, "priority": priority, "due": due})

def show(filter_pending=False, sort_by=None):
    items = [t for t in todos if not (filter_pending and t["done"])]
    if sort_by == "priority":
        order = {"높음": 0, "보통": 1, "낮음": 2}
        items.sort(key=lambda t: order[t["priority"]])
    for i, t in enumerate(items, 1):
        mark = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {mark}[{t['priority']}] {t['task']} (~{t['due']})")
```

**도전 과제**
- 마감일 임박(D-day≤3) 항목 강조
- 카테고리(태그) 추가, `list --tag work`

---

### 과제 6. 단어장 퀴즈 (확장판)

**목표**: 영단어 사전으로 랜덤 퀴즈 + 양방향 모드 + 복습 모드

**필요 사전지식**: 기초 7주차(딕셔너리) + 8주차(문자열) + `random` 모듈

**기초 과제와의 차별점**
- 기초 종합 예시 = **단순 출제 + 점수**
- 실습 6번 = **양방향(영↔한) + 복습 모드(틀린 문제만) + 통계**

**요구사항**
- 단어장은 딕셔너리 (`{"apple": "사과", ...}`)
- 모드 선택: 1.영→한 2.한→영 3.랜덤
- 10문제 출제, 정답/오답 즉시 피드백
- 마지막에 점수 + 틀린 단어 목록
- 복습 모드: 틀린 단어만 다시 출제

**입출력 예시**
```
모드(1.영→한 2.한→영 3.랜덤): 1
[1/10] apple의 뜻은? 사과
정답!
[2/10] book의 뜻은? 가방
오답. 정답: 책
...
총점: 7 / 10
틀린 단어: book, table, door
복습할까요? (y/n): y
[1/3] book의 뜻은? ...
```

**도전 과제**
- 단어장을 외부 파일(JSON/CSV)에서 로드
- 정답률 통계를 단어별로 누적 저장 (어려운 단어 우선 출제)

---

### 과제 7. 주소록

**목표**: 이름·전화·이메일 검색·수정·삭제 CLI

**필요 사전지식**: 기초 7주차(딕셔너리) + 8주차(문자열)

**요구사항**
- 데이터 구조: `{"홍길동": {"phone": "010-...", "email": "..."}}`
- 명령: `add`, `find <키워드>`, `update <이름>`, `del <이름>`, `list`
- 부분 일치 검색 (`"홍"` 입력 → 홍길동, 홍철수 모두)
- 이름 정렬 출력

**도전 과제**
- 같은 이름 처리 (이름 뒤에 일련번호 붙이기)
- 전화번호 형식 검증 (정규표현식 — 중급 9주차 선행 필요)

---

### 과제 8. BMI 추적기

**목표**: 여러 명의 BMI를 입력받아 분류 + 정렬 표 출력

**필요 사전지식**: 기초 6주차(리스트) + 9주차(함수) + f-string 정렬

**기초 과제와의 차별점**
- 기초 3주차 = **1명 BMI 계산 + 분류 출력**
- 실습 8번 = **N명 입력 + 정렬 표 + 통계 + 카테고리별 집계**

**요구사항**
- 사용자별로 이름·키·몸무게 입력 (`done` 입력 시 종료)
- 분류: 저체중(<18.5), 정상(18.5~23), 과체중(23~25), 비만(>=25)
- 표 형태로 정렬 출력 (BMI 내림차순)

**입출력 예시**
```
이름      키(cm)  몸무게(kg)  BMI    분류
홍길동    175     70          22.86  정상
김영희    160     45          17.58  저체중
평균 BMI: 20.22 (정상 범위)
```

**도전 과제**
- 분류별 인원수 집계 출력
- 결과를 CSV로 저장

---

## Lv ★★★ — 중급 종합 (파일·예외·OOP)

### 과제 9. 가계부

**목표**: 수입/지출을 파일에 영구 저장하는 가계부

**필요 사전지식**: 중급 5주차(예외) + 6주차(파일 I/O — JSON)

**요구사항**
- JSON 파일로 저장 (`ledger.json`) — 종료 후에도 데이터 보존
- 명령: `add 수입|지출 금액 카테고리 메모`, `list`, `summary`, `del <번호>`
- 카테고리별 합계, 잔액 출력
- 잘못된 입력(음수 금액, 파일 손상)은 예외 처리

**핵심 코드 힌트**
```python
import json
from pathlib import Path

FILE = Path("ledger.json")

def load():
    if not FILE.exists():
        return []
    try:
        return json.loads(FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("ledger.json 손상 — 빈 장부로 시작")
        return []

def save(records):
    FILE.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
```

**도전 과제**
- 월별 집계 (`2026-05` 같은 형식으로 필터)
- 카테고리별 막대그래프 출력 (`#` 문자로)
- 입력을 한 줄 명령으로 (`add 지출 5000 식비 점심`)

---

### 과제 10. 도서 관리 시스템

**목표**: 도서 등록·대출·반납 CLI (OOP 적용)

**필요 사전지식**: 중급 6주차(파일 I/O) + 7주차(클래스) + 8주차(상속)

**요구사항**
- `Book` 클래스: title, author, isbn, is_borrowed, borrower
- `Member` 클래스: name, member_id, borrowed_books
- `Library` 클래스: 도서·회원 목록 관리, `borrow()`, `return_book()` 메서드
- 명령: `book add`, `book list`, `member add`, `borrow <isbn> <member_id>`, `return <isbn>`, `search <키워드>`
- JSON 파일에 영구 저장

**핵심 코드 힌트**
```python
from dataclasses import dataclass, field, asdict
from typing import Optional

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    is_borrowed: bool = False
    borrower: Optional[str] = None

class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.members: list[Member] = []

    def borrow(self, isbn: str, member_id: str) -> bool:
        book = next((b for b in self.books if b.isbn == isbn and not b.is_borrowed), None)
        if not book:
            raise ValueError(f"대출 불가: {isbn}")
        book.is_borrowed = True
        book.borrower = member_id
        return True
```

**도전 과제**
- 대출 기간 / 연체 일수 계산 (`datetime`)
- 회원별 대출 이력 출력

---

### 과제 11. 일기장

**목표**: 날짜별 일기 작성·조회·검색 CLI

**필요 사전지식**: 중급 4주차(`datetime`, `pathlib`) + 6주차(파일 I/O)

**요구사항**
- 일기는 `diary/YYYY-MM-DD.txt`로 저장
- 명령: `write` (오늘 일기), `read <날짜>`, `list`, `search <키워드>`
- 같은 날짜 다시 쓰면 덮어쓸지 물어보기
- 다중 행 입력 (빈 줄 두 번 → 종료)

**도전 과제**
- 키워드 검색 시 매치된 일기의 해당 줄과 날짜 함께 출력
- 작성 통계 (총 작성일 수, 평균 길이, 가장 긴 일기)

---

### 과제 12. 텍스트 어드벤처 게임

**목표**: 분기 선택형 어드벤처 게임 (5장면 이상, 다중 엔딩)

**필요 사전지식**: 중급 6주차(JSON I/O) + 7주차(클래스 — 선택)

**요구사항**
- 최소 5개 이상의 장면(scene), 분기 3회 이상
- HP/아이템 등 상태 관리
- 엔딩 분기 2개 이상
- 시나리오는 외부 JSON 파일에서 로드

**핵심 코드 힌트**
```python
import json
from pathlib import Path

scenes = json.loads(Path("scenario.json").read_text(encoding="utf-8"))
state = {"hp": 100, "items": []}
current = "start"

while current != "end":
    s = scenes[current]
    print(s["text"])
    for k, choice in s["choices"].items():
        print(f"  {k}. {choice['label']}")
    pick = input("> ")
    next_id = s["choices"][pick]["next"]
    # 효과 적용 (HP 감소, 아이템 획득 등)
    if "effect" in s["choices"][pick]:
        ...
    current = next_id
```

**도전 과제**
- 게임 진행 상황 저장/불러오기 (`save`, `load` 명령)
- 시나리오 편집기 (CLI로 새 장면 추가)

---

## Lv ★★★★ — 고급 응용 (CLI 도구화)

### 과제 13. argparse 기반 CLI 도구

**목표**: 진짜 CLI 도구처럼 인자/옵션을 받는 프로그램 (서브커맨드 구조)

**필요 사전지식**: 고급 1주차(타입 힌트) + 9주차(패키징) + 중급 6주차(파일 I/O)

**요구사항**
- `argparse` 의 서브커맨드(`subparsers`) 사용
- `mytool add ...`, `mytool list`, `mytool del ...` 형태
- `--help`, `--version` 동작
- 예: 실습 5번 To-Do 또는 실습 9번 가계부를 argparse로 재작성
- `pyproject.toml` 의 `[project.scripts]` 로 등록

**입출력 예시**
```
$ todo add "우유 사기" --priority high --due 2026-05-15
$ todo list --only-pending
$ todo done 3
$ todo --version
todo 1.0.0
```

**핵심 코드 힌트**
```python
import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="todo")
    p.add_argument("--version", action="version", version="todo 1.0.0")
    sub = p.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add")
    add.add_argument("task")
    add.add_argument("--priority", choices=["low", "high"], default="low")
    add.add_argument("--due")

    sub.add_parser("list").add_argument("--only-pending", action="store_true")
    return p
```

**도전 과제**
- `click` 라이브러리로 재작성하고 비교
- 컬러 출력 (`rich` 라이브러리)

---

### 과제 14. CSV 데이터 분석 CLI

**목표**: CSV 파일을 받아 자동 통계 리포트 생성

**필요 사전지식**: 고급 8주차(NumPy/Pandas) — 또는 중급 6주차(`csv` 모듈)만 사용

**요구사항**
- 입력: `python analyze.py sales.csv`
- 컬럼 자동 감지 → 숫자 컬럼은 평균/최대/최소/합계, 문자 컬럼은 빈도 Top 5
- pandas 또는 표준 `csv` 모듈 (선택)
- 결과를 콘솔과 `report.txt` 양쪽에 출력

**입출력 예시**
```
$ python analyze.py sales.csv
[행 수] 1000
[숫자: price]
  평균: 12,345  최대: 99,000  최소: 1,000  합계: 12,345,000
[숫자: quantity]
  평균: 3.2    최대: 50      최소: 1
[문자: category]
  food   : 412
  drink  : 280
  daily  : 187
  ...
report.txt 저장 완료
```

**도전 과제**
- 필터 옵션 (`--column price --min 10000`)
- 결과를 CSV/JSON 양쪽으로 export
- matplotlib으로 막대그래프 PNG 생성

---

### 과제 15. 콘솔 챗봇

**목표**: 콘솔 기반 챗봇 (규칙 기반 또는 LLM API)

**필요 사전지식**: 고급 7주차(requests) + 5주차(asyncio — 선택)

**요구사항**
- 사용자 입력 ↔ 응답 반복
- 종료 명령(`/quit`, `/exit`)
- 대화 이력 저장 (JSON)
- 명령어 모드: `/clear`, `/save`, `/load`, `/history`

**선택 옵션**
- A. **규칙 기반**: 키워드/정규표현식 매칭 응답
- B. **API 기반**: `requests`로 LLM API 호출 (API 키는 `.env` + `python-dotenv`)

**핵심 코드 힌트 (API 기반)**
```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def ask(messages: list[dict]) -> str:
    r = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": os.environ["ANTHROPIC_API_KEY"],
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={"model": "claude-haiku-4-5-20251001", "max_tokens": 1024, "messages": messages},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["content"][0]["text"]
```

**도전 과제**
- 토큰 사용량 표시
- 비동기로 여러 모델에 동시 질의 후 비교 (`asyncio` + `httpx`)

---

### 과제 16. TUI 앱 (rich/textual)

**목표**: 터미널에 풍부한 UI를 그리는 앱

**필요 사전지식**: 고급 1주차(타입 힌트) + 외부 라이브러리(`rich` 또는 `textual`)

**요구사항**
- `rich` 또는 `textual` 라이브러리 사용
- 표, 진행 바, 패널, 컬러 지원
- 예: 실습 5번 To-Do 또는 실습 9번 가계부를 TUI로 재작성
- 키보드 단축키 1개 이상

**핵심 코드 힌트 (rich)**
```python
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="To-Do", show_lines=True)
table.add_column("번호", style="cyan", justify="right")
table.add_column("상태")
table.add_column("우선순위", style="magenta")
table.add_column("할 일")

for i, t in enumerate(todos, 1):
    mark = "[green]완료[/]" if t["done"] else "[yellow]진행[/]"
    table.add_row(str(i), mark, t["priority"], t["task"])

console.print(table)
```

**도전 과제**
- `textual` 로 풀스크린 TUI + 키보드 단축키
- 실시간 갱신(자동 새로고침) — `Live` 또는 `textual.timer`

---

## 제출 가이드

각 과제 제출물은 다음을 포함합니다.

1. **소스 코드**: `.py` 파일 (필요 시 모듈 분리)
2. **README.md**: 실행 방법, 사용한 문법/라이브러리, 예시 실행 화면
3. **시연**: 스크린샷 또는 짧은 녹화(1분 이내)
4. **회고 (선택)**: 어려웠던 점, 배운 점

### 디렉토리 구조 권장 예시

```
project_name/
├── README.md
├── pyproject.toml         (Lv ★★★★ 권장)
├── main.py
├── requirements.txt        (외부 라이브러리 사용 시)
├── tests/                  (Lv ★★★~ 권장)
│   └── test_main.py
└── data/
    └── sample.json
```

---

## 채점 기준

| 항목 | 비중 | 설명 |
|------|------|------|
| 동작(요구사항 충족) | 40% | 명세대로 동작하는가 |
| 코드 품질 | 25% | 함수/클래스 분리, 변수명, 들여쓰기, 타입 힌트 |
| 예외 처리 | 15% | 잘못된 입력, 빈 데이터, 파일 없음 등 |
| 응용·도전 과제 | 20% | 추가 기능 구현 여부 |

Lv ★★★~★★★★ 는 **테스트(pytest) 작성** 가산점 +10%.

---

## 학습 흐름 추천

```
[기초 과정 학습자]
    Lv ★ (가위바위보, 숫자 맞추기, 계산기, 단위 변환기)
        ↓
    Lv ★★ (To-Do, 단어장 퀴즈, 주소록, BMI 추적기)

[중급 과정 학습자]
    + Lv ★★★ (가계부, 도서 관리, 일기장, 텍스트 어드벤처)

[고급 과정 학습자]
    + Lv ★★★★ (argparse CLI, CSV 분석, 챗봇, TUI 앱)
```

| 학습자 단계 | 권장 도전 범위 |
|------------|----------------|
| 기초만 이수 | Lv ★ ~ Lv ★★ |
| 중급까지 이수 | Lv ★ ~ Lv ★★★ |
| 고급까지 이수 | Lv ★ ~ Lv ★★★★ (전체) |
