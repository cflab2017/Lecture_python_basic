from dataclasses import dataclass, field
from datetime import date

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    is_borrowed: bool = False

@dataclass
class Member:
    member_id: str
    name: str
    borrowed: list[str] = field(default_factory=list)

@dataclass
class Loan:
    isbn: str
    member_id: str
    borrowed_date: date
    due_date: date

    def is_overdue(self) -> bool:
        return date.today() > self.due_date

# 데모
b = Book("Python", "Guido", "978-1")
m = Member("M001", "홍길동")
loan = Loan("978-1", "M001", date(2026, 5, 1), date(2026, 5, 15))
print(b)
print(m)
print(loan, "연체:", loan.is_overdue())
