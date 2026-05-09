import pandas as pd
from io import StringIO

CSV = """name,dept,score
Alice,A,92
Bob,B,78
Charlie,A,85
Dave,B,67
Eve,A,94
Frank,C,71
"""

df = pd.read_csv(StringIO(CSV))

print("[학과별 평균]")
print(df.groupby("dept")["score"].mean())

print(f"\n[전체 통계]")
print(f"평균: {df.score.mean():.2f}")
top_idx = df.score.idxmax()
print(f"최고: {df.loc[top_idx, 'name']} ({df.loc[top_idx, 'score']})")
