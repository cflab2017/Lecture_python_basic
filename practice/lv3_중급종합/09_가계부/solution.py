"""가계부 — JSON 영구 저장"""
import json
from pathlib import Path
from datetime import date

DB = Path("ledger.json")

def load():
    if not DB.exists():
        return []
    try:
        return json.loads(DB.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("⚠️ ledger.json 손상 — 빈 장부로 시작")
        return []

def save(records):
    DB.write_text(
        json.dumps(records, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

def add(records):
    t = input("수입/지출: ").strip()
    if t not in ("수입", "지출"):
        print("'수입' 또는 '지출'"); return
    try:
        amount = int(input("금액: "))
        if amount < 0:
            raise ValueError
    except ValueError:
        print("양의 정수 입력"); return
    category = input("카테고리: ").strip()
    memo = input("메모: ").strip()
    records.append({
        "type": t, "amount": amount, "category": category,
        "memo": memo, "date": date.today().isoformat(),
    })
    save(records)
    print("추가됨")

def show(records):
    if not records:
        print("(비어있음)"); return
    for i, r in enumerate(records, 1):
        sign = "+" if r["type"] == "수입" else "-"
        print(f"{i:>3}. {r['date']} {sign}{r['amount']:>10,}원 [{r['category']:<6}] {r['memo']}")

def summary(records):
    income = sum(r["amount"] for r in records if r["type"] == "수입")
    expense = sum(r["amount"] for r in records if r["type"] == "지출")
    print(f"수입: {income:>12,}원")
    print(f"지출: {expense:>12,}원")
    print(f"잔액: {income - expense:>12,}원")

    by_cat = {}
    for r in records:
        if r["type"] == "지출":
            by_cat[r["category"]] = by_cat.get(r["category"], 0) + r["amount"]
    if by_cat:
        max_amt = max(by_cat.values())
        print("\n[지출 카테고리별]")
        for cat, amt in sorted(by_cat.items(), key=lambda x: -x[1]):
            bar = "#" * int(40 * amt / max_amt)
            print(f"  {cat:<8} {amt:>10,}  {bar}")

def main():
    records = load()
    print(f"불러옴: {len(records)}건")
    while True:
        cmd = input("\n명령(add/list/summary/del <n>/quit): ").strip()
        if not cmd: continue
        if cmd == "quit": break
        elif cmd == "add": add(records)
        elif cmd == "list": show(records)
        elif cmd == "summary": summary(records)
        elif cmd.startswith("del "):
            try:
                idx = int(cmd.split()[1]) - 1
                if 0 <= idx < len(records):
                    del records[idx]; save(records); print("삭제")
            except (ValueError, IndexError):
                print("올바른 번호 입력")

if __name__ == "__main__":
    main()
