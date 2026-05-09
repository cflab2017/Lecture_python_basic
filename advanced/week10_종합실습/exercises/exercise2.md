# 최종 과제 2. CLI 도구 패키지

## 목표
실용적인 CLI 도구를 만들고 PyPI 또는 TestPyPI에 배포.

## 요구사항
- `pyproject.toml` 기반 패키지 구조
- `argparse` 또는 `click` 으로 CLI
- 외부 API 호출 (날씨, 환율, GitHub 등)
- 타입 힌트 + mypy 통과
- pytest 테스트
- TestPyPI 업로드 검증

## 아이디어
- 환율 변환기 (실시간 환율 API)
- 날씨 알림 (지역 입력 → 5일 예보)
- GitHub Stars 추적기
