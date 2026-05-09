import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dave", "Eve"],
    "score": [92, 78, 85, 67, 94],
    "dept": ["A", "B", "A", "B", "A"],
})

print(df)
print()
print("describe():")
print(df.describe())
print()
print("shape:", df.shape)
print("columns:", df.columns.tolist())
print("dtypes:")
print(df.dtypes)

# 행/열 선택
print("\n점수 컬럼:")
print(df["score"])
print("\n행 0:")
print(df.iloc[0])
