# 과제 3. Vector 클래스 (2D)

## 요구사항
- `Vector(x, y)` 생성자
- `+`, `-` 오버로딩
- `==` (같은 좌표면 True)
- `__repr__` (`Vector(1, 2)` 형태)
- `magnitude()` — 크기(피타고라스)

## 사용 예
```python
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)         # Vector(4, 6)
print(v1.magnitude())  # 5.0
print(v1 == Vector(3, 4))   # True
```
