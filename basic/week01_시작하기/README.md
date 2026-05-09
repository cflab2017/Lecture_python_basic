# 1주차. 파이썬 시작하기

> 단계: 기초 | 선수: 없음

## 학습 목표
- 프로그래밍 언어와 인터프리터의 차이를 설명할 수 있다
- 파이썬 개발 환경(Python + VS Code)을 직접 설치한다
- 첫 파이썬 프로그램을 작성하고 실행한다
- REPL과 스크립트의 차이를 이해한다
- 주석을 사용해 코드에 설명을 단다

## 1. 파이썬이란

파이썬(Python)은 1991년 귀도 반 로섬(Guido van Rossum)이 발표한 **인터프리터 언어**입니다. 사람이 읽기 쉬운 문법으로 설계되어 입문자가 가장 먼저 배우기 좋은 언어로 꼽힙니다.

활용 분야:
- 웹 개발 (Django, FastAPI)
- 데이터 분석·머신러닝 (Pandas, PyTorch)
- 자동화·스크립팅
- 게임, 임베디드, 교육 등

**컴파일 vs 인터프리터**: 파이썬은 코드를 한 줄씩 즉시 실행합니다. 따라서 빠른 시제품 제작에 강점이 있지만, C/Java처럼 미리 컴파일하는 언어보다는 실행 속도가 느립니다.

## 2. 개발 환경 설치

### Python 설치
- 공식 사이트: <https://www.python.org/downloads/>
- 버전: **3.10 이상** 권장
- Windows: 설치 시 **"Add Python to PATH"** 체크 필수
- macOS: `brew install python` 도 가능

### 설치 확인
터미널(또는 명령 프롬프트)에서:
```bash
python --version       # Python 3.x.x
python3 --version      # macOS/Linux는 보통 python3
```

### VS Code 설치
- <https://code.visualstudio.com/>
- 확장(Extensions)에서 **"Python"** (Microsoft) 설치

## 3. 첫 프로그램 — Hello, World!

### REPL (대화형 모드)
터미널에서 `python` 입력 → `>>>` 프롬프트가 뜸 → 한 줄씩 입력하고 즉시 결과 확인.
```
>>> print("Hello, Python!")
Hello, Python!
>>> exit()
```

### 스크립트 모드
파일에 코드를 저장하고 실행. 이쪽이 실제 개발의 기본.
```bash
# hello.py 라는 파일 작성 후
python hello.py
```

→ examples/01_hello.py 참고.

## 4. 주석

`#` 으로 시작하면 그 줄 끝까지 주석. 컴퓨터는 무시하고, 사람만 읽는다.
```python
# 한 줄 주석
print("실행됨")    # 줄 끝에도 가능
```

여러 줄 주석은 `"""..."""` 으로도 표현하지만, 이는 엄밀히는 문자열입니다.

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_hello.py` | `print()` 로 첫 출력 |
| `02_multiple_print.py` | 여러 줄 출력 |
| `03_comments.py` | 주석 사용법 |

## ⚠️ 자주 하는 실수

1. **터미널에서 `python` 명령어가 안 됨**
   → Windows에서 PATH 등록 누락. 설치 마법사 다시 실행 후 "Add Python to PATH" 체크.

2. **"SyntaxError: Missing parentheses in call to 'print'"**
   → Python 2 문법 (`print "hello"`)을 사용. Python 3는 반드시 괄호 사용 (`print("hello")`).

3. **한글이 깨짐**
   → 파일 저장 시 인코딩이 UTF-8이 아닌 경우. VS Code 우하단 인코딩 표시 확인.

4. **`print(Hello)` 처럼 따옴표를 빼먹음**
   → `NameError: name 'Hello' is not defined`. 문자열은 반드시 `"..."` 또는 `'...'` 로 감싸야 함.

## ❓ 자주 묻는 질문 (FAQ)

**Q1. `python` 과 `python3` 의 차이는?**
A. macOS/Linux에는 시스템 Python 2가 함께 깔려 있어서 `python3` 으로 명시해야 하는 경우가 많습니다. Windows는 보통 `python` 만으로 동작합니다. 둘 다 시도해보세요.

**Q2. VS Code 말고 다른 에디터를 써도 되나요?**
A. 네. PyCharm, Sublime Text, 메모장도 가능합니다. 다만 자동완성·디버깅이 없는 환경은 학습 효율이 떨어집니다.

**Q3. REPL과 스크립트 중 어느 쪽을 써야 하나요?**
A. 짧은 실험·확인은 REPL, 실제 프로그램은 스크립트입니다. 수업에서는 둘 다 자주 사용합니다.

**Q4. `print` 외에 다른 출력 방법은 없나요?**
A. `sys.stdout.write()` 등 더 저수준 함수도 있지만, 입문 단계에서는 `print()` 만으로 충분합니다.

## 📝 과제 (exercises/)

- `exercise1.md` — 환경 설치 인증
- `exercise2.md` — `intro.py` 자기소개 출력
- `exercise3.md` — 자기소개 카드 (`print` 5개 이상)

## 정답 (solutions/)

먼저 직접 풀어보고 막힐 때만 `solutions/` 참고.

## 다음 주차

[2주차. 변수와 자료형](../week02_변수와_자료형/) — 데이터를 변수에 담아 다루는 법
