"""단어장 앱 — 진입점"""
from pathlib import Path
from models import WordBook

def main():
    book = WordBook(Path("words.json"))
    while True:
        cmd = input("\n명령(add/list/del/quiz/quit): ").strip()
        if cmd == "quit":
            break
        elif cmd == "add":
            en = input("영어: ")
            ko = input("뜻: ")
            book.add(en, ko)
        elif cmd == "list":
            for w in book.words:
                print(f"  {w.en} - {w.ko}")
        elif cmd == "del":
            en = input("삭제할 영어: ")
            ok = book.remove(en)
            print("삭제됨" if ok else "없음")
        elif cmd == "quiz":
            score, total = book.quiz(5)
            print(f"\n점수: {score} / {total}")

if __name__ == "__main__":
    main()
