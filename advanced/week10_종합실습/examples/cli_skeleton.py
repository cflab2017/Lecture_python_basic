"""argparse + 모듈 분리 CLI 골격"""
import argparse
from pathlib import Path
import json

def cmd_add(args):
    db = Path(args.db)
    items = json.loads(db.read_text(encoding="utf-8")) if db.exists() else []
    items.append({"id": len(items) + 1, "task": args.task})
    db.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"추가됨: {args.task}")

def cmd_list(args):
    db = Path(args.db)
    if not db.exists():
        print("(비어있음)"); return
    for it in json.loads(db.read_text(encoding="utf-8")):
        print(f"{it['id']}. {it['task']}")

def main():
    parser = argparse.ArgumentParser(prog="todo")
    parser.add_argument("--db", default="todos.json")
    parser.add_argument("--version", action="version", version="todo 0.1.0")

    sub = parser.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add")
    add.add_argument("task")
    add.set_defaults(func=cmd_add)

    lst = sub.add_parser("list")
    lst.set_defaults(func=cmd_list)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
