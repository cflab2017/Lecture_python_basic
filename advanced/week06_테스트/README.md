# 6주차. 테스트 (unittest, pytest)

> 단계: 고급 | 선수: 5주차

## 학습 목표
- pytest 기본 사용법
- `parametrize` 로 다양한 케이스
- `fixture` 로 공통 setup
- mock 으로 외부 의존성 격리

## 1. 왜 테스트?

- 회귀 방지 (코드 변경 시 동작 보장)
- 명세 역할 (의도 문서화)
- 리팩토링 안전망

## 2. pytest 기본

```bash
pip install pytest
```

테스트 파일은 `test_*.py` 또는 `*_test.py`.

```python
# test_calc.py
def add(a, b): return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

```bash
pytest                  # 전체 실행
pytest test_calc.py     # 한 파일
pytest -v               # verbose
pytest -k "add"         # 이름 매칭
```

## 3. parametrize

같은 테스트를 여러 입력으로.

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## 4. fixture

공통 setup 코드.

```python
@pytest.fixture
def sample_users():
    return [{"name": "Alice"}, {"name": "Bob"}]

def test_first(sample_users):
    assert sample_users[0]["name"] == "Alice"

def test_count(sample_users):
    assert len(sample_users) == 2
```

스코프 (`session`, `module`, `function`):
```python
@pytest.fixture(scope="module")
def expensive():
    print("한 번만 setup")
    return ...
```

## 5. 예외 검증

```python
def divide(a, b):
    if b == 0:
        raise ValueError("0 division")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError, match="0 division"):
        divide(10, 0)
```

## 6. mock

외부 의존성(API, DB)을 가짜로.

```python
from unittest.mock import patch, MagicMock

def get_weather(city):
    import requests
    return requests.get(f"https://api/{city}").json()

def test_get_weather():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"temp": 20}
        assert get_weather("seoul") == {"temp": 20}
```

## 7. 커버리지

```bash
pip install pytest-cov
pytest --cov=mypackage --cov-report=term-missing
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_basic_test.py` | 기본 assert |
| `02_parametrize.py` | parametrize |
| `03_fixture.py` | fixture |
| `04_mock.py` | unittest.mock |

## ⚠️ 자주 하는 실수

1. **테스트 함수가 `test_` 로 시작 안 함** — pytest가 못 찾음
2. **테스트끼리 의존** — 실행 순서가 바뀌면 깨짐. 독립적으로
3. **전역 상태 변경** — fixture로 setup/teardown
4. **외부 API 진짜로 호출** — 느리고 불안정. mock 사용

## ❓ FAQ

**Q1. unittest 와 pytest 중?**
A. 표준은 unittest. 신규 프로젝트는 pytest 압도적 권장 (간결, 강력).

**Q2. TDD 를 꼭 해야 하나요?**
A. 아니지만 권장. 최소한 핵심 기능은 테스트.

**Q3. UI 테스트는?**
A. Selenium, Playwright 등 별도 도구.

## 📝 과제 (exercises/)

- `exercise1.md` — 중급 OOP 코드 테스트
- `exercise2.md` — parametrize 다양한 케이스
- `exercise3.md` — mock 으로 API 호출 테스트

## 다음 주차

[7주차. 웹 스크래핑](../week07_웹_스크래핑/)
