import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
    (1.5, 2.5, 4.0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# id 부여
@pytest.mark.parametrize("score,grade", [
    (95, "A"),
    (85, "B"),
    (75, "C"),
    (50, "F"),
], ids=["A학점", "B학점", "C학점", "F학점"])
def test_grade(score, grade):
    def to_grade(s):
        if s >= 90: return "A"
        if s >= 80: return "B"
        if s >= 70: return "C"
        return "F"
    assert to_grade(score) == grade
