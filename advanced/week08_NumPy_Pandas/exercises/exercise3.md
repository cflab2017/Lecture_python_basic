# 과제 3. 매출 피벗 테이블

## 입력
```csv
date,category,amount
2026-01-15,food,12000
2026-01-20,drink,5000
2026-02-03,food,8500
2026-02-10,daily,3200
...
```

## 출력 (피벗)
```
category    daily  drink   food
date
2026-01         0   5000  12000
2026-02      3200      0   8500
```

## 힌트
```python
df["date"] = pd.to_datetime(df["date"]).dt.to_period("M")
pivot = df.pivot_table(index="date", columns="category",
                      values="amount", aggfunc="sum", fill_value=0)
```
