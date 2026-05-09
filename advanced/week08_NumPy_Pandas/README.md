# 8주차. NumPy / Pandas 입문

> 단계: 고급 | 선수: 7주차

## 학습 목표
- NumPy 배열 생성·연산·인덱싱
- Pandas DataFrame 기본
- CSV 읽기·필터·집계
- groupby 와 피벗 테이블

```bash
pip install numpy pandas matplotlib
```

## 1. NumPy 기본

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a.mean(), a.std(), a.sum())

# 벡터 연산 (Python list보다 훨씬 빠름)
print(a * 2)        # [2 4 6 8 10]
print(a + a)
print(a > 2)        # 불리언 배열

# 2D
m = np.arange(12).reshape(3, 4)
print(m)
print(m.shape)
print(m.sum(axis=0))   # 컬럼 합
print(m.sum(axis=1))   # 행 합
```

## 2. NumPy 인덱싱

```python
a = np.arange(10)
print(a[3])
print(a[2:6])
print(a[a > 5])      # 불리언 인덱싱

m = np.arange(12).reshape(3, 4)
print(m[1, 2])       # 행 1, 열 2
print(m[:, 1])       # 모든 행, 열 1
print(m[1, :])       # 행 1
```

## 3. Pandas DataFrame

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Dave"],
    "score": [92, 78, 85, 67],
    "dept": ["A", "B", "A", "B"],
})

print(df)
print(df.describe())
print(df.shape, df.columns.tolist())
```

## 4. 필터·정렬·집계

```python
# 필터
print(df[df.score >= 80])

# 정렬
print(df.sort_values("score", ascending=False))

# 그룹 집계
print(df.groupby("dept")["score"].mean())
print(df.groupby("dept").agg({"score": ["mean", "max", "count"]}))
```

## 5. CSV 읽기

```python
df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])
monthly = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()
print(monthly)
```

## 6. 시각화 (matplotlib)

```python
import matplotlib.pyplot as plt

monthly.plot(kind="bar")
plt.title("월별 매출")
plt.tight_layout()
plt.savefig("monthly.png")
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `01_numpy_basic.py` | 배열, 연산 |
| `02_numpy_indexing.py` | 인덱싱·슬라이싱 |
| `03_pandas_basic.py` | DataFrame 생성·조회 |
| `04_pandas_groupby.py` | 필터·groupby |

## ⚠️ 자주 하는 실수

1. **for 루프로 NumPy 배열 처리** — 벡터 연산 사용해야 빠름
2. **`SettingWithCopyWarning`** — `df[df.x > 0]["y"] = 5` 대신 `.loc[]` 사용
3. **인덱스 vs 컬럼 혼동** — `df["a"]` 는 컬럼, `df.loc[a]` 는 인덱스
4. **NaN 무시** — `dropna()`, `fillna()` 로 명시적 처리

## ❓ FAQ

**Q1. NumPy 와 list 의 차이?**
A. NumPy는 동일 타입, 메모리 연속, 벡터 연산. 수치 계산에서 100배 이상 빠름.

**Q2. Pandas 와 SQL 의 차이?**
A. Pandas는 메모리 내 데이터프레임. SQL은 영구 저장 + 큰 데이터. 분석은 Pandas, 운영 데이터는 SQL.

**Q3. polars 가 더 빠르다는데?**
A. 맞음. 큰 데이터에서 더 좋음. 다만 생태계는 pandas 가 압도적.

## 📝 과제 (exercises/)

- `exercise1.md` — students.csv 학과별 통계
- `exercise2.md` — NumPy 시뮬레이션 (BMI 1000명)
- `exercise3.md` — 매출 피벗 테이블

## 다음 주차

[9주차. 패키징과 배포](../week09_패키징_배포/)
