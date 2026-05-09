contacts = {}

while True:
    cmd = input("명령(add/find/del/list/quit): ").strip()
    if cmd == "quit":
        break
    elif cmd == "add":
        name = input("이름: ")
        phone = input("전화: ")
        contacts[name] = phone
        print("추가됨")
    elif cmd == "find":
        name = input("이름: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("찾을 수 없습니다")
    elif cmd == "del":
        name = input("이름: ")
        if name in contacts:
            del contacts[name]
            print("삭제됨")
        else:
            print("없는 이름입니다")
    elif cmd == "list":
        for i, (name, phone) in enumerate(contacts.items(), 1):
            print(f"{i}. {name}: {phone}")
