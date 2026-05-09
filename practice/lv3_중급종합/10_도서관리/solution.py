"""도서 관리 — OOP + JSON"""
import json
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import Optional

DB = Path("library.json")

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    is_borrowed: bool = False
    borrower: Optional[str] = None

@dataclass
class Member:
    member_id: str
    name: str
    borrowed: list[str] = field(default_factory=list)

class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.members: list[Member] = []
        self.load()

    def load(self):
        if not DB.exists(): return
        data = json.loads(DB.read_text(encoding="utf-8"))
        self.books = [Book(**b) for b in data.get("books", [])]
        self.members = [Member(**m) for m in data.get("members", [])]

    def save(self):
        DB.write_text(json.dumps({
            "books": [asdict(b) for b in self.books],
            "members": [asdict(m) for m in self.members],
        }, ensure_ascii=False, indent=2), encoding="utf-8")

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save()

    def add_member(self, mid, name):
        self.members.append(Member(mid, name))
        self.save()

    def borrow(self, isbn, member_id):
        book = next((b for b in self.books if b.isbn == isbn and not b.is_borrowed), None)
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not book: raise ValueError(f"대출 불가: {isbn}")
        if not member: raise ValueError(f"회원 없음: {member_id}")
        book.is_borrowed = True
        book.borrower = member_id
        member.borrowed.append(isbn)
        self.save()

    def return_book(self, isbn):
        book = next((b for b in self.books if b.isbn == isbn and b.is_borrowed), None)
        if not book: raise ValueError(f"반납 불가: {isbn}")
        member = next((m for m in self.members if m.member_id == book.borrower), None)
        if member: member.borrowed.remove(isbn)
        book.is_borrowed = False
        book.borrower = None
        self.save()

    def search(self, keyword):
        return [b for b in self.books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]

def main():
    lib = Library()
    while True:
        raw = input("\n> ").strip()
        if not raw: continue
        if raw == "quit": break
        try:
            parts = raw.split()
            cmd = parts[0]
            if cmd == "book" and parts[1] == "add":
                t = input("제목: "); a = input("저자: "); i = input("ISBN: ")
                lib.add_book(t, a, i); print("등록됨")
            elif cmd == "book" and parts[1] == "list":
                for b in lib.books:
                    status = f"대출중({b.borrower})" if b.is_borrowed else "보유"
                    print(f"  [{status}] {b.title} / {b.author} / {b.isbn}")
            elif cmd == "member" and parts[1] == "add":
                m = input("ID: "); n = input("이름: ")
                lib.add_member(m, n); print("등록됨")
            elif cmd == "borrow":
                lib.borrow(parts[1], parts[2]); print("대출 완료")
            elif cmd == "return":
                lib.return_book(parts[1]); print("반납 완료")
            elif cmd == "search":
                results = lib.search(parts[1])
                for b in results:
                    print(f"  {b.title} / {b.author}")
        except (IndexError, ValueError) as e:
            print(f"에러: {e}")

if __name__ == "__main__":
    main()
