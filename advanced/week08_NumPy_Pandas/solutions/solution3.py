import pandas as pd
from io import StringIO

CSV = """date,category,amount
2026-01-15,food,12000
2026-01-20,drink,5000
2026-02-03,food,8500
2026-02-10,daily,3200
2026-02-15,drink,4800
2026-03-01,food,15000
2026-03-12,daily,2700
"""

df = pd.read_csv(StringIO(CSV))
df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")

pivot = df.pivot_table(
    index="month", columns="category",
    values="amount", aggfunc="sum", fill_value=0
)
print(pivot)
print("\n월별 합계:")
print(pivot.sum(axis=1))
