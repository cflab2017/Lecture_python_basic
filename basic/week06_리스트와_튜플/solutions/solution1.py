scores = []
for i in range(1, 6):
    s = int(input(f"{i}번 학생 점수: "))
    scores.append(s)

total = sum(scores)
avg = total / len(scores)
print(f"\n총점: {total}")
print(f"평균: {avg:.1f}")
print(f"최고점: {max(scores)}")
print(f"최저점: {min(scores)}")
