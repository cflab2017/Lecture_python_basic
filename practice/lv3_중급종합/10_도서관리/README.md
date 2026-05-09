# 과제 10. 도서 관리 시스템

> 난이도: Lv ★★★ | 사전지식: 중급 6-8주차 (파일 I/O, OOP)

## 목표
도서 등록·대출·반납 CLI (OOP 적용)

## 요구사항
- `Book`, `Member`, `Library` 클래스
- 명령: `book add`, `book list`, `member add`, `borrow <isbn> <member_id>`, `return <isbn>`, `search <키워드>`
- JSON 영구 저장

## 도전 과제
- 대출 기간/연체 일수 (`datetime`)
- 회원별 대출 이력
