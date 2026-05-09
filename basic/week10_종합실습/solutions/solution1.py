"""최종 과제 1 — 콘솔 To-Do List 해답"""

todos = []

def add(task):
    todos.append({"task": task, "done": False})

def show():
    if not todos:
        print("(할 일 없음)")
        return
    for i, t in enumerate(todos, 1):
        mark = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {mark} {t['task']}")

def mark_done(idx):
    if 1 <= idx <= len(todos):
        todos[idx - 1]["done"] = True
        print(f"{idx}번 완료")
    else:
        print("그런 번호 없음")

def remove(idx):
    if 1 <= idx <= len(todos):
        del todos[idx - 1]
        print(f"{idx}번 삭제")
    else:
        print("그런 번호 없음")

while True:
    raw = input("\n> ").strip()
    if not raw:
        continue
    parts = raw.split(maxsplit=1)
    cmd = parts[0]
    arg = parts[1] if len(parts) > 1 else ""

    if cmd == "quit":
        break
    elif cmd == "add":
        if arg:
            add(arg)
            print("추가됨")
        else:
            print("할 일을 입력하세요")
    elif cmd == "list":
        show()
    elif cmd == "done":
        try:
            mark_done(int(arg))
        except ValueError:
            print("번호를 입력하세요")
    elif cmd == "del":
        try:
            remove(int(arg))
        except ValueError:
            print("번호를 입력하세요")
    else:
        print("알 수 없는 명령")
