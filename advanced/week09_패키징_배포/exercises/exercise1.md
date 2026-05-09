# 과제 1. 중급 종합실습 결과를 패키지로

## 목표
중급 10주차의 단어장 앱을 `pyproject.toml` 기반 패키지로 변환.

## 요구사항
```
wordbook/
├── pyproject.toml
├── src/wordbook/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   └── cli.py
└── README.md
```

## 검증
```bash
pip install -e .
wordbook --help
```
