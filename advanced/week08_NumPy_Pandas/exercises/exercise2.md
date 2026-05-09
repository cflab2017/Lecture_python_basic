# 과제 2. NumPy 시뮬레이션 (BMI 1000명)

## 목표
- 키 1000명 (정규분포: 평균 170cm, 표준편차 8)
- 몸무게 1000명 (정규분포: 평균 65kg, 표준편차 10)
- BMI 계산
- 분류별 인원 출력 (저체중/정상/과체중/비만)

## 힌트
```python
heights = np.random.normal(170, 8, 1000)
weights = np.random.normal(65, 10, 1000)
bmi = weights / (heights / 100) ** 2
```
