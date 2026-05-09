import numpy as np

np.random.seed(42)

heights = np.random.normal(170, 8, 1000)
weights = np.random.normal(65, 10, 1000)
bmi = weights / (heights / 100) ** 2

print(f"평균 BMI: {bmi.mean():.2f}")
print(f"분포: {bmi.min():.1f} ~ {bmi.max():.1f}")
print()

# 분류
underweight = (bmi < 18.5).sum()
normal = ((bmi >= 18.5) & (bmi < 23)).sum()
overweight = ((bmi >= 23) & (bmi < 25)).sum()
obese = (bmi >= 25).sum()

print(f"저체중: {underweight}명 ({underweight/10:.1f}%)")
print(f"정상  : {normal}명 ({normal/10:.1f}%)")
print(f"과체중: {overweight}명 ({overweight/10:.1f}%)")
print(f"비만  : {obese}명 ({obese/10:.1f}%)")
