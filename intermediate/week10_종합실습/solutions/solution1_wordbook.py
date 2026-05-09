"""단어장 해답 — 단일 파일 버전 (실제는 패키지로 분리 권장)"""
import json
import random
from dataclasses import dataclass, asdict
from pathlib import Path

DB = Path("words_solution.json")

@dataclass
class Word:
    en: str
    ko: str

def load():
    if not DB.exists():
        return []
    return [Word(**d) for d in json.loads(DB.read_text(encoding="utf-8"))]

def save(words):
    DB.write_text(
        json.dumps([asdict(w) for w in words], ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

def main():
    words = load()
    print(f"로드: {len(words)}개")
    while True:
        cmd = input("\n> ").strip().lower()
        if cmd == "quit":
            save(words); break
        elif cmd == "add":
            en = input("영어: ")
            ko = input("뜻: ")
            words.append(Word(en, ko)); save(words)
        elif cmd == "list":
            for w in words: print(f"  {w.en}: {w.ko}")
        elif cmd == "quiz":
            n = min(5, len(words))
            if n == 0:
                print("단어 없음"); continue
            sample = random.sample(words, n)
            score = 0
            for i, w in enumerate(sample, 1):
                a = input(f"[{i}/{n}] {w.en}? ")
                if a == w.ko:
                    score += 1; print("정답")
                else:
                    print(f"오답. 정답: {w.ko}")
            print(f"점수: {score}/{n}")

if __name__ == "__main__":
    main()
