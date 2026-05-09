# 과제 3. 호출 횟수 카운터

## 목표
함수 호출 횟수를 누적하는 클로저 `make_counter()` 작성.

## 요구사항
- `c = make_counter()` 후 `c()` 호출할 때마다 1씩 증가하며 현재 값 반환
- `c1`, `c2` 처럼 여러 개를 만들면 각각 독립적

## 입출력 예시
```python
c1 = make_counter()
c2 = make_counter()
print(c1())   # 1
print(c1())   # 2
print(c1())   # 3
print(c2())   # 1
print(c1())   # 4
```
