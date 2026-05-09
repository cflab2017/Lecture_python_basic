# 과제 3. 파일 읽기 예외 처리

## 목표
파일 경로를 입력받아 내용을 출력. 다양한 예외를 처리.

## 처리할 예외
- `FileNotFoundError` — "파일 없음: ..."
- `PermissionError` — "권한 없음: ..."
- `UnicodeDecodeError` — "인코딩 오류: ..."

## 사용 예
```
경로: data.txt
파일 없음: data.txt

경로: /etc/shadow
권한 없음: /etc/shadow
```
