import pytest

def grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    return "F"

@pytest.mark.parametrize("score,expected", [
    (100, "A"), (95, "A"), (90, "A"),
    (89, "B"), (85, "B"), (80, "B"),
    (79, "C"), (75, "C"), (70, "C"),
    (69, "D"), (65, "D"), (60, "D"),
    (59, "F"), (30, "F"), (0, "F"),
    (-10, "F"),
])
def test_grade(score, expected):
    assert grade(score) == expected
