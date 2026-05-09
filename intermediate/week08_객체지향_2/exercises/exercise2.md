# 과제 2. Playlist 클래스

## 요구사항
- 곡 추가/삭제, 인덱스로 곡 가져오기
- `len(playlist)` 동작
- `for song in playlist:` 동작
- `song in playlist` 동작
- `__repr__` 도 구현

## 사용 예
```python
p = Playlist()
p.add("Bohemian Rhapsody")
p.add("Imagine")
print(len(p))
print(p[0])
print("Imagine" in p)
for song in p:
    print(song)
```
