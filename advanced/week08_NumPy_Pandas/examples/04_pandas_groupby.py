import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dave", "Eve"],
    "score": [92, 78, 85, 67, 94],
    "dept": ["A", "B", "A", "B", "A"],
})

# 필터
print("80점 이상:")
print(df[df.score >= 80])

# 정렬
print("\n점수 내림차순:")
print(df.sort_values("score", ascending=False))

# groupby
print("\n학과별 평균:")
print(df.groupby("dept")["score"].mean())

print("\n학과별 다양한 집계:")
print(df.groupby("dept").agg(
    avg=("score", "mean"),
    high=("score", "max"),
    n=("score", "count"),
))
