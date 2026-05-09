"""기초 과정 마지막 주차 — To-Do List 골격
이 코드를 확장해 add/done/del/quit 명령을 모두 지원해보세요.
"""

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

def done(idx):
    if 1 <= idx <= len(todos):
        todos[idx - 1]["done"] = True

# main 루프
while True:
    cmd = input("\n명령(add/show/done/quit): ").strip()
    if cmd == "quit":
        break
    elif cmd == "add":
        task = input("할 일: ")
        add(task)
    elif cmd == "show":
        show()
    elif cmd == "done":
        idx = int(input("번호: "))
        done(idx)
    else:
        print("알 수 없는 명령")
