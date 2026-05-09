# 9주차. 패키징과 배포

> 단계: 고급 | 선수: 8주차

## 학습 목표
- `pyproject.toml` 의 구조를 이해한다
- 자체 패키지를 빌드해서 설치한다
- `console_scripts` 로 CLI 도구 제공
- 가상환경(`venv`)
- TestPyPI 업로드

## 1. 가상환경

프로젝트마다 라이브러리 버전 분리.

```bash
python -m venv .venv

# 활성화
source .venv/bin/activate         # macOS/Linux
.venv\Scripts\activate            # Windows

# 종료
deactivate
```

## 2. pyproject.toml

현대 파이썬 패키지의 표준 설정 파일.

```toml
[project]
name = "mytool"
version = "0.1.0"
description = "내 멋진 CLI 도구"
authors = [{name = "홍길동", email = "hong@example.com"}]
requires-python = ">=3.10"
dependencies = [
    "requests>=2.28",
    "rich>=13.0",
]

[project.scripts]
mytool = "mytool.cli:main"

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"
```

## 3. 패키지 구조

```
mytool_project/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── mytool/
│       ├── __init__.py
│       └── cli.py
└── tests/
    └── test_cli.py
```

```python
# src/mytool/cli.py
def main():
    print("Hello from mytool!")
```

설치:
```bash
pip install -e .          # 개발 모드 (수정이 즉시 반영)
mytool                    # CLI 실행
```

## 4. 빌드

```bash
pip install build
python -m build           # dist/ 에 .whl, .tar.gz 생성
```

## 5. TestPyPI 업로드

```bash
pip install twine
twine upload --repository testpypi dist/*
```

다른 환경에서 설치:
```bash
pip install --index-url https://test.pypi.org/simple/ mytool
```

## 6. requirements.txt vs pyproject.toml

| | requirements.txt | pyproject.toml |
|---|------------------|----------------|
| 용도 | 환경 고정 (deploy) | 라이브러리 메타데이터 |
| 버전 | 정확한 핀 | 범위 |
| 빌드 | 안 됨 | 됨 |

```bash
pip freeze > requirements.txt   # 현재 환경 내보내기
pip install -r requirements.txt # 재현
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `pyproject.toml` | 패키지 설정 |
| `src/mytool/__init__.py` | 패키지 |
| `src/mytool/cli.py` | CLI 진입점 |
| `README_PROJECT.md` | 패키지 README 예시 |

## ⚠️ 자주 하는 실수

1. **가상환경 활성화 안 함** — 시스템 파이썬에 설치됨
2. **`__init__.py` 빠뜨림** — 패키지로 인식 안 됨
3. **`src/` 레이아웃 안 씀** — import 충돌 가능
4. **버전 안 올리고 재배포** — PyPI는 같은 버전 재업로드 거부

## ❓ FAQ

**Q1. setup.py 는 안 쓰나요?**
A. 신규는 `pyproject.toml`. 레거시 호환만 setup.py.

**Q2. poetry vs pip+venv?**
A. poetry는 통합 도구 (의존성 + 가상환경 + 빌드). 신규는 poetry나 uv 권장.

**Q3. PyPI 와 TestPyPI 차이?**
A. PyPI는 진짜 공개. TestPyPI는 연습용.

## 📝 과제 (exercises/)

- `exercise1.md` — 중급 종합실습 결과를 패키지로
- `exercise2.md` — console_scripts CLI 설치
- `exercise3.md` — TestPyPI 업로드

## 다음 주차

[10주차. 고급 종합 실습](../week10_종합실습/)
