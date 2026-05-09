# 과제 2. parametrize 다양한 케이스

## 목표
함수 하나에 대해 parametrize 로 10개 이상 케이스를 검증한다.

## 예: 학점 계산 함수
```python
def grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    return "F"
```

테스트해야 할 케이스:
- 경계값 (89, 90)
- 음수, 100 초과
- 정상 케이스 4-5개
