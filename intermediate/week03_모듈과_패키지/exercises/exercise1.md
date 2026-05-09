# 과제 1. calculator/ 패키지

## 목표
사칙연산 + 고급(제곱, 루트) 두 모듈로 분리된 패키지를 만든다.

## 구조
```
calculator/
├── __init__.py     # add, sub, mul, div, power, sqrt 모두 export
├── basic.py        # add, sub, mul, div
└── advanced.py     # power, sqrt
```

## 사용 예
```python
from calculator import add, power, sqrt
print(add(3, 5))      # 8
print(power(2, 10))   # 1024
print(sqrt(16))       # 4.0
```
