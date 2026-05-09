import csv

with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score", "dept"])
    writer.writerows([
        ["Alice", 92, "A"],
        ["Bob", 78, "B"],
        ["Charlie", 85, "A"],
    ])

print("scores.csv 생성됨")

# DictWriter로 더 명확하게
with open("scores2.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "score": 92})
    writer.writerow({"name": "Bob", "score": 78})

print("scores2.csv 생성됨")
