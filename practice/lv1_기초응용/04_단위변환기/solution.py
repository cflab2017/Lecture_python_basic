"""단위 변환기 — 다중 카테고리 + 양방향"""

def cm_to_inch(cm): return cm / 2.54
def inch_to_cm(inch): return inch * 2.54
def kg_to_lb(kg): return kg * 2.2046226218
def lb_to_kg(lb): return lb / 2.2046226218
def c_to_f(c): return c * 9 / 5 + 32
def f_to_c(f): return (f - 32) * 5 / 9

def menu_length():
    direction = input("1.cm→inch 2.inch→cm: ").strip()
    val = float(input("값: "))
    if direction == "1":
        print(f"{val} cm = {cm_to_inch(val):.2f} inch")
    else:
        print(f"{val} inch = {inch_to_cm(val):.2f} cm")

def menu_weight():
    direction = input("1.kg→lb 2.lb→kg: ").strip()
    val = float(input("값: "))
    if direction == "1":
        print(f"{val} kg = {kg_to_lb(val):.2f} lb")
    else:
        print(f"{val} lb = {lb_to_kg(val):.2f} kg")

def menu_temp():
    direction = input("1.°C→°F 2.°F→°C: ").strip()
    val = float(input("값: "))
    if direction == "1":
        print(f"{val}°C = {c_to_f(val):.2f}°F")
    else:
        print(f"{val}°F = {f_to_c(val):.2f}°C")

def main():
    handlers = {"1": menu_length, "2": menu_weight, "3": menu_temp}
    while True:
        choice = input("\n[메뉴] 1.길이 2.무게 3.온도 4.종료: ").strip()
        if choice == "4":
            break
        if choice in handlers:
            handlers[choice]()

if __name__ == "__main__":
    main()
