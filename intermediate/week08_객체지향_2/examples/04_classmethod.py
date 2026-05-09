class Date:
    def __init__(self, y, m, d):
        self.y, self.m, self.d = y, m, d

    def __repr__(self):
        return f"Date({self.y}, {self.m}, {self.d})"

    @classmethod
    def from_string(cls, s):
        y, m, d = map(int, s.split("-"))
        return cls(y, m, d)

    @staticmethod
    def is_valid(y, m, d):
        return 1 <= m <= 12 and 1 <= d <= 31

d = Date.from_string("2026-05-09")
print(d)
print(Date.is_valid(2026, 5, 9))
print(Date.is_valid(2026, 13, 1))
