# 과제 13. argparse 기반 CLI 도구

> 난이도: Lv ★★★★ | 사전지식: 고급 1, 9주차

## 목표
서브커맨드 구조를 갖춘 진짜 CLI 도구 (예: To-Do)

## 요구사항
- argparse 의 subparsers
- `mytool add ...`, `mytool list`, `mytool del ...`
- `--help`, `--version` 동작
- pyproject.toml 의 console_scripts 로 등록 가능

## 입출력 예시
```
$ todo add "우유 사기" --priority high
$ todo list --only-pending
$ todo done 3
$ todo --version
```

## 도전 과제
- `click` 으로 재작성 비교
- `rich` 컬러 출력
