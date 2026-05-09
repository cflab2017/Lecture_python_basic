# 과제 3. Optional/list/dict 시그니처

## 목표
다음 함수들의 시그니처를 타입 힌트와 함께 작성한다 (구현은 자유).

1. `find_book(isbn: str) -> Optional[Book]`
2. `list_books(tag: Optional[str] = None) -> list[Book]`
3. `borrow_count_by_member() -> dict[str, int]`
4. `register(member: Member, books: list[Book]) -> bool`
5. `apply_filter(items: list[Book], pred: Callable[[Book], bool]) -> list[Book]`

각 함수는 docstring + 타입 힌트가 명확해야 합니다.
