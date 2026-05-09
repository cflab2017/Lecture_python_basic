"""최종 과제 3 — 가계부 해답"""

records = []

def add():
    t = input("수입/지출: ").strip()
    if t not in ("수입", "지출"):
        print("'수입' 또는 '지출'만 가능"); return
    amount = int(input("금액: "))
    category = input("카테고리: ").strip()
    memo = input("메모: ").strip()
    records.append({"type": t, "amount": amount, "category": category, "memo": memo})
    print("추가됨")

def show():
    for i, r in enumerate(records, 1):
        sign = "+" if r["type"] == "수입" else "-"
        print(f"{i}. {sign}{r['amount']:,}원 [{r['category']}] {r['memo']}")

def summary():
    income = sum(r["amount"] for r in records if r["type"] == "수입")
    expense = sum(r["amount"] for r in records if r["type"] == "지출")
    print(f"수입: {income:,}원")
    print(f"지출: {expense:,}원")
    print(f"잔액: {income - expense:,}원")

    by_cat = {}
    for r in records:
        if r["type"] == "지출":
            by_cat[r["category"]] = by_cat.get(r["category"], 0) + r["amount"]
    if by_cat:
        print("\n[지출 카테고리별]")
        for cat, amt in sorted(by_cat.items(), key=lambda x: -x[1]):
            print(f"{cat}: {amt:,}원")

while True:
    cmd = input("\n명령(add/list/summary/quit): ").strip()
    if cmd == "quit": break
    elif cmd == "add": add()
    elif cmd == "list": show()
    elif cmd == "summary": summary()
