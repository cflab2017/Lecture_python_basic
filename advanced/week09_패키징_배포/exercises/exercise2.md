# 과제 2. console_scripts CLI 설치

## 목표
패키지를 설치하면 터미널에서 `mytool` 명령으로 직접 실행되도록.

## 요구사항
- `pyproject.toml` 의 `[project.scripts]` 활용
- `pip install -e .` 후 `mytool` 명령 동작 확인

## 입출력 예시
```bash
$ pip install -e .
$ mytool --version
mytool 0.1.0
$ mytool --name Alice
Hello, Alice!
```
