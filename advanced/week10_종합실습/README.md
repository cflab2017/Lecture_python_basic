# 10주차. 고급 종합 실습

> 단계: 고급 | 선수: 1~9주차 전부

## 학습 목표
- 비동기·외부 라이브러리·테스트·배포를 통합한 실전 프로젝트
- 패키지 구조 + CI 적용

## 1. 프로젝트 구조 (권장)

```
my_project/
├── pyproject.toml
├── README.md
├── src/my_project/
│   ├── __init__.py
│   ├── models.py        (dataclass)
│   ├── client.py        (httpx 비동기)
│   ├── analyzer.py      (Pandas)
│   └── cli.py           (argparse 진입점)
├── tests/
│   ├── test_models.py
│   ├── test_client.py
│   └── test_analyzer.py
└── .github/workflows/ci.yml   (선택)
```

## 2. 골격 — 비동기 크롤러 + 분석

`examples/crawler_skeleton.py` 참고.

## 3. 체크리스트

- [ ] 타입 힌트 + `mypy --strict`
- [ ] pytest 테스트 (커버리지 70%+)
- [ ] CLI (`argparse` 또는 `click`)
- [ ] 비동기 또는 병렬 처리
- [ ] 외부 라이브러리 (requests/httpx, pandas 등)
- [ ] `pyproject.toml` 패키지화
- [ ] README (설치법, 사용법)

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `crawler_skeleton.py` | 비동기 크롤링 + Pandas 분석 골격 |
| `cli_skeleton.py` | argparse + 모듈 분리 골격 |

## ⚠️ 자주 하는 실수

1. **모놀리식 한 파일** — 테스트도 어렵고 재사용도 어려움
2. **타입 힌트 누락** — IDE 지원 안 받음
3. **테스트 없이 시작** — 나중에 붙이기 더 어려움
4. **README 없음** — 본인도 며칠 후 잊어버림

## ❓ FAQ

**Q1. CI 가 뭔가요?**
A. Continuous Integration. GitHub Actions 등으로 push마다 자동 테스트.

**Q2. 어떤 도메인을 골라야 하나요?**
A. 본인이 진짜 쓸 만한 것. 예: 매일 아침 뉴스 요약, 공부 시간 추적, 코인 시세 알림.

## 📝 최종 과제 (exercises/)

다음 4개 중 1개 선택.

1. `exercise1.md` — **비동기 크롤러 + 분석**
2. `exercise2.md` — **CLI 도구 패키지** (PyPI 배포)
3. `exercise3.md` — **데이터 파이프라인** (CSV → 정제 → 시각화)
4. `exercise4.md` — **자동화 봇** (Slack/Discord 웹훅)

## 제출물
- GitHub 저장소 링크
- 실행 영상 또는 스크린샷
- README (설치, 사용법, 예시)
- pytest 테스트
- (선택) PyPI 또는 TestPyPI 링크

## 다음 단계

고급 과정을 마쳤습니다! 🎉

본격 도메인 학습:
- **백엔드**: FastAPI / Django REST framework
- **데이터·ML**: PyTorch / scikit-learn / Hugging Face
- **자동화·DevOps**: Ansible / Airflow / Docker
- **웹 스크래핑**: Scrapy / Playwright

실습 도전: [../../practice/lv4_고급응용](../../practice/lv4_고급응용/) (argparse CLI, CSV 분석, 챗봇, TUI 앱)
