# 과제 1. chunked_lines(path, n)

## 목표
파일을 N줄씩 묶어 yield 하는 제너레이터.

## 사용 예
```python
for chunk in chunked_lines("big.txt", 100):
    process(chunk)   # 100줄씩 처리
```
