class InvalidScoreError(Exception):
    pass

def validate_score(s):
    if not (0 <= s <= 100):
        raise InvalidScoreError(f"0~100 범위여야 합니다: {s}")

def grade(s):
    validate_score(s)
    if s >= 90: return "A"
    if s >= 80: return "B"
    if s >= 70: return "C"
    if s >= 60: return "D"
    return "F"

while True:
    try:
        score = int(input("점수: "))
        print(f"학점: {grade(score)}")
        break
    except (ValueError, InvalidScoreError) as e:
        print("실패:", e)
