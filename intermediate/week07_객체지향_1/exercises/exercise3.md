# 과제 3. Student 클래스

## 요구사항
- 속성: `name`, `scores: list[int]`
- 메서드:
  - `add_score(s)`
  - `average()` — 평균
  - `highest()` — 최고점
  - `passed(threshold=60)` — 평균이 threshold 이상이면 True

## 사용 예
```python
s = Student("홍길동")
s.add_score(85); s.add_score(92); s.add_score(78)
print(s.average())   # 85.0
print(s.passed())    # True
```
