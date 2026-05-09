height_cm = float(input("키(cm): "))
weight_kg = float(input("몸무게(kg): "))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

print(f"당신의 BMI는 {bmi:.2f} 입니다.")
