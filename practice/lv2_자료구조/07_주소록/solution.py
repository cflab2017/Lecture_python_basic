"""주소록 — 부분 일치 검색"""

contacts = {}

def add():
    name = input("이름: ").strip()
    if not name: return
    phone = input("전화: ").strip()
    email = input("이메일: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print("추가됨")

def find(query):
    matched = [(n, c) for n, c in contacts.items() if query.lower() in n.lower()]
    if not matched:
        print("없음"); return
    for name, c in matched:
        print(f"  {name} | {c['phone']} | {c['email']}")

def show_all():
    for name in sorted(contacts):
        c = contacts[name]
        print(f"  {name}: {c['phone']}, {c['email']}")

def main():
    while True:
        raw = input("\n명령(add/find <q>/del <name>/list/quit): ").strip()
        if not raw: continue
        parts = raw.split(maxsplit=1)
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else ""
        if cmd == "quit": break
        elif cmd == "add": add()
        elif cmd == "find":
            if arg: find(arg)
            else: print("키워드 입력")
        elif cmd == "del":
            if arg in contacts:
                del contacts[arg]; print("삭제")
            else:
                print("없음")
        elif cmd == "list":
            show_all()

if __name__ == "__main__":
    main()
