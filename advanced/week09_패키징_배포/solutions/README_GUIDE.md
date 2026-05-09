# 해답 가이드 — 패키징 단계별

## 1. 폴더 구조 만들기

```
wordbook/
├── pyproject.toml
├── README.md
├── src/
│   └── wordbook/
│       ├── __init__.py
│       ├── models.py     (중급 10주차 코드)
│       └── cli.py
└── tests/
    └── test_models.py
```

## 2. pyproject.toml

```toml
[project]
name = "wordbook"
version = "0.1.0"
description = "콘솔 단어장 앱"
requires-python = ">=3.10"

[project.scripts]
wordbook = "wordbook.cli:main"

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"
```

## 3. 설치

```bash
cd wordbook
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -e .
wordbook                      # 즉시 실행
```

## 4. 빌드

```bash
pip install build
python -m build
ls dist/
# wordbook-0.1.0-py3-none-any.whl
# wordbook-0.1.0.tar.gz
```

## 5. TestPyPI 업로드

```bash
pip install twine
twine upload --repository testpypi dist/*
```

## 6. 다른 환경에서 검증

```bash
python -m venv test_env && source test_env/bin/activate
pip install --index-url https://test.pypi.org/simple/ wordbook
wordbook
```
