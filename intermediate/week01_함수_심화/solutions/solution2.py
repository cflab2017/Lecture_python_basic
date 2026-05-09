students = [
    {"name": "홍길동", "score": 85},
    {"name": "김영희", "score": 92},
    {"name": "이철수", "score": 78},
]

ranked = sorted(students, key=lambda s: -s["score"])
for i, s in enumerate(ranked, 1):
    print(f"{i}등: {s['name']} ({s['score']}점)")
