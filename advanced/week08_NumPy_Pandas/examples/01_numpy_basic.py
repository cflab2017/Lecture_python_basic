import numpy as np

a = np.array([1, 2, 3, 4, 5])
print("array:", a)
print("mean:", a.mean(), "std:", a.std(), "sum:", a.sum())

# 벡터 연산
print("a * 2:", a * 2)
print("a + a:", a + a)
print("a > 2:", a > 2)

# 2D
m = np.arange(12).reshape(3, 4)
print(m)
print("shape:", m.shape)
print("axis=0 합:", m.sum(axis=0))
print("axis=1 합:", m.sum(axis=1))

# 통계
print("min/max/median:", m.min(), m.max(), np.median(m))
