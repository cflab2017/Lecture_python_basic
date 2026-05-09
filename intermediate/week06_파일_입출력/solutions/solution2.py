import csv
from pathlib import Path

# 데모용 입력 파일 생성
Path("students.csv").write_text(
    "name,score\nAlice,92\nBob,78\nCharlie,85\nDave,67\n",
    encoding="utf-8"
)

with open("students.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

scores = [(r["name"], int(r["score"])) for r in rows]
total = sum(s for _, s in scores)
avg = total / len(scores)
top = max(scores, key=lambda x: x[1])
bot = min(scores, key=lambda x: x[1])

print(f"학생 수: {len(scores)}명")
print(f"평균: {avg:.2f}")
print(f"최고: {top[0]} ({top[1]})")
print(f"최저: {bot[0]} ({bot[1]})")

Path("students.csv").unlink()
