"""BMI 추적기 — 다인원 + 정렬 표"""

def classify(bmi):
    if bmi < 18.5: return "저체중"
    if bmi < 23: return "정상"
    if bmi < 25: return "과체중"
    return "비만"

def main():
    people = []
    print("이름 자리에 'done' 입력 시 종료")
    while True:
        name = input("\n이름: ").strip()
        if name.lower() == "done": break
        try:
            h = float(input("키(cm): "))
            w = float(input("몸무게(kg): "))
        except ValueError:
            print("숫자만"); continue
        bmi = w / (h / 100) ** 2
        people.append({"name": name, "h": h, "w": w, "bmi": bmi})

    if not people:
        return

    people.sort(key=lambda p: -p["bmi"])
    print(f"\n{'이름':<10}{'키':>7}{'몸무게':>9}{'BMI':>9}  분류")
    for p in people:
        print(f"{p['name']:<10}{p['h']:>7.1f}{p['w']:>9.1f}{p['bmi']:>9.2f}  {classify(p['bmi'])}")

    avg = sum(p["bmi"] for p in people) / len(people)
    print(f"\n평균 BMI: {avg:.2f} ({classify(avg)})")

    # 분류별 집계
    counts = {}
    for p in people:
        c = classify(p["bmi"])
        counts[c] = counts.get(c, 0) + 1
    print("\n[분류별]")
    for c in ["저체중", "정상", "과체중", "비만"]:
        print(f"  {c}: {counts.get(c, 0)}명")

if __name__ == "__main__":
    main()
