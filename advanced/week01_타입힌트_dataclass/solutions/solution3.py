from typing import Optional, Callable
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    isbn: str
    tags: list[str]

@dataclass
class Member:
    member_id: str
    name: str

def find_book(isbn: str) -> Optional[Book]:
    """ISBN 으로 책을 찾는다. 없으면 None"""
    ...

def list_books(tag: Optional[str] = None) -> list[Book]:
    """tag 필터로 책 리스트. None이면 전체"""
    ...

def borrow_count_by_member() -> dict[str, int]:
    """회원별 대출 횟수"""
    ...

def register(member: Member, books: list[Book]) -> bool:
    """member에게 books 모두 대출. 성공 여부"""
    ...

def apply_filter(items: list[Book], pred: Callable[[Book], bool]) -> list[Book]:
    """조건 함수로 필터링"""
    return [b for b in items if pred(b)]

# 데모
books = [Book("A", "1", ["py"]), Book("B", "2", ["js"])]
print(apply_filter(books, lambda b: "py" in b.tags))
