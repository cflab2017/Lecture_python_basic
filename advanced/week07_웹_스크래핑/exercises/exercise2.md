# 과제 2. GitHub 사용자 저장소 정보

## 목표
GitHub API로 특정 사용자의 공개 저장소 목록과 별 개수를 출력.

## 엔드포인트
`https://api.github.com/users/{username}/repos`

## 출력 예시
```
사용자: python
저장소 개수: 30
1. cpython - 50000 stars
2. python-docs-translations - 200 stars
...
```

## 도전
- 정렬 (별 개수 내림차순)
- pagination (per_page=100)
