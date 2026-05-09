# 과제 1. Shape 계층

## 요구사항
- `Shape` 추상 클래스 (`area()` 와 `perimeter()` 정의)
- `Rectangle(width, height)` 와 `Circle(radius)` 가 상속
- 각 메서드를 정확히 계산
- `__repr__` 도 구현

## 사용 예
```python
shapes = [Rectangle(3, 4), Circle(5)]
for s in shapes:
    print(s, "→ 면적:", s.area(), "둘레:", s.perimeter())
```
