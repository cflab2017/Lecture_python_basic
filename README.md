# Lecture_python_basic

파이썬 강의 커리큘럼 + 주차별 실행 가능한 예제 코드 + 과제 + 해답.
**기초 / 중급 / 고급 / 실습과제** 4단계 구성.

## 디렉토리 구조

```
Lecture_python_basic/
├── README.md                         이 파일
├── curriculum_basic.md               기초 과정 전체 개요
├── curriculum_intermediate.md        중급 과정 전체 개요
├── curriculum_advanced.md            고급 과정 전체 개요
├── curriculum_practice.md            실습과제 카탈로그
├── basic/                            기초 과정 (10주차)
│   ├── README.md                     과정 인덱스
│   └── week01_시작하기/
│       ├── README.md                 수업 노트 (개념 + FAQ + 실수)
│       ├── examples/*.py             수업 예제 (실행 가능)
│       ├── exercises/*.md, *.py      과제 명세 + 시작 코드
│       └── solutions/*.py            과제 해답
├── intermediate/                     중급 과정 (10주차)
├── advanced/                         고급 과정 (10주차)
└── practice/                         실습과제 (CLI 16개)
    ├── lv1_기초응용/                 ★      (4개)
    ├── lv2_자료구조/                 ★★    (4개)
    ├── lv3_중급종합/                 ★★★  (4개)
    └── lv4_고급응용/                 ★★★★(4개)
```

## 과정 안내

| 단계 | 인덱스 | 개요 문서 | 분량 |
|------|--------|----------|------|
| 1. 기초 | [basic/](./basic/) | [curriculum_basic.md](./curriculum_basic.md) | 10주 |
| 2. 중급 | [intermediate/](./intermediate/) | [curriculum_intermediate.md](./curriculum_intermediate.md) | 10주 |
| 3. 고급 | [advanced/](./advanced/) | [curriculum_advanced.md](./curriculum_advanced.md) | 10주 |
| 4. 실습과제 | [practice/](./practice/) | [curriculum_practice.md](./curriculum_practice.md) | CLI 16개 |

## 사용법 (학생용)

```bash
# 1. 저장소 클론
git clone https://github.com/cflab2017/Lecture_python_basic.git
cd Lecture_python_basic

# 2. 원하는 주차 폴더로 이동
cd basic/week01_시작하기

# 3. 수업 노트 읽기
cat README.md

# 4. 예제 코드 실행해보기
python examples/01_hello.py

# 5. 과제 풀어보기
cat exercises/exercise1.md
# → exercises/ 안에 본인 풀이 작성

# 6. 해답 확인
python solutions/solution1.py
```

## 학습 흐름

```
기초 (10주)  →  중급 (10주)  →  고급 (10주)
                                              ↘
                                   실습과제 (난이도 ★~★★★★)
```

| 학습자 단계 | 권장 실습 범위 |
|------------|----------------|
| 기초만 이수 | Lv ★ ~ ★★ |
| 중급까지 이수 | Lv ★ ~ ★★★ |
| 고급까지 이수 | Lv ★ ~ ★★★★ (전체) |

## 단계별 핵심 주제

- **기초**: 자료형, 연산자, 입출력, 조건문, 반복문, 리스트/튜플/딕셔너리/집합, 문자열, 함수 기초
- **중급**: 함수 심화, 컴프리헨션·제너레이터, 모듈/패키지, 표준 라이브러리, 예외 처리, 파일 입출력, 객체지향, 정규표현식
- **고급**: 타입 힌트·dataclass, 데코레이터·컨텍스트 매니저, 동시성(threading/asyncio), 테스트, 웹 스크래핑, NumPy·Pandas, 패키징·배포
- **실습과제**: CLI 프로젝트 16개 — 가위바위보·숫자 맞추기 → To-Do·단어장 → 가계부·도서 관리 → argparse·TUI

## 수업 형식 (공통)

- 회당 2시간, 이론 30% / 라이브 코딩 예제 40% / 실습 30%
- 매 주차 **3~4개의 핵심 예제** 직접 작성, **2~3개의 과제** 제출
- 각 과정 종료 시 종합 프로젝트
