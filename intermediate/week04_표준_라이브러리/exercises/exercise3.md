# 과제 3. 단어 빈도 Top 5 (Counter)

## 목표
긴 텍스트에서 가장 많이 등장한 단어 5개를 출력한다.

## 요구사항
- `collections.Counter` 사용
- 대소문자 구분 없이
- 마침표·콤마 등 제거

## 힌트
```python
import re
words = re.findall(r"\w+", text.lower())
```
