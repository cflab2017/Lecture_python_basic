# 과제 2. Book / Member / Loan dataclass

## 요구사항
- 도서관 시스템의 핵심 모델 3개를 `@dataclass` 로 작성

```python
@dataclass
class Book: ...     # title, author, isbn, is_borrowed=False
@dataclass
class Member: ...   # member_id, name, borrowed: list[str]
@dataclass
class Loan: ...     # isbn, member_id, borrowed_date, due_date
```

- `Loan.is_overdue()` 메서드 (오늘 > due_date)
