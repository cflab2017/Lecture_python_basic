# 과제 3. 큰 파일 라인 단위 제너레이터

## 목표
파일을 한 줄씩 yield 하는 제너레이터 `read_lines(path)` 작성.

## 요구사항
- 큰 파일을 한 번에 메모리에 로드하지 않음
- 빈 줄과 공백 제외 (strip 후 비어있으면 skip)

## 사용 예
```python
for line in read_lines("data.txt"):
    print(line)
```

## 도전
- N줄씩 묶어 yield 하는 `chunked_lines(path, n)` 도 작성
