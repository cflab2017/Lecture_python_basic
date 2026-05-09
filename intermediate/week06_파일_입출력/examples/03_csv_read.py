import csv

# 위 예제로 만들어진 파일을 읽음
with open("scores.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(f"{row['name']}: {row['score']}점 ({row['dept']}반)")

# 정리
import os
for fn in ("scores.csv", "scores2.csv"):
    if os.path.exists(fn):
        os.remove(fn)
