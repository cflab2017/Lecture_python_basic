import numpy as np

a = np.arange(10)
print(a[3])
print(a[2:6])

# 불리언 인덱싱
print("> 5인 것:", a[a > 5])

# 2D
m = np.arange(12).reshape(3, 4)
print(m)
print("(1, 2):", m[1, 2])
print("열 1:", m[:, 1])
print("행 1:", m[1, :])

# fancy 인덱싱
print(m[[0, 2], [1, 3]])   # (0,1), (2,3) 위치

# 조건부 변경
m_copy = m.copy()
m_copy[m_copy > 5] = -1
print(m_copy)
