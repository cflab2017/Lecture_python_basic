# 과제 3. TestPyPI 업로드

## 목표
실제로 패키지를 빌드하고 TestPyPI 에 올린다.

## 요구사항
- TestPyPI 계정 생성 (https://test.pypi.org)
- API 토큰 발급
- `pip install build twine`
- `python -m build`
- `twine upload --repository testpypi dist/*`
- 다른 환경에서 설치 검증:
  ```bash
  pip install --index-url https://test.pypi.org/simple/ <패키지명>
  ```

## 주의
- 패키지 이름은 PyPI 전역에서 유일해야 함
- 같은 버전 재업로드 불가 → 버전 업
