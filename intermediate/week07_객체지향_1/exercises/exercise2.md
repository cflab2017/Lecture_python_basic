# 과제 2. Stack 클래스

## 요구사항
- LIFO (후입선출)
- 메서드: `push(x)`, `pop()`, `peek()`, `is_empty()`, `__len__()`
- 빈 스택에서 pop/peek 시 예외

## 사용 예
```python
s = Stack()
s.push(1); s.push(2); s.push(3)
print(s.peek())   # 3
print(len(s))     # 3
print(s.pop())    # 3
```
