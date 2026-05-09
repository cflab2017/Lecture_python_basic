"""단어장 앱 — 모델 정의"""
from dataclasses import dataclass, asdict
from pathlib import Path
import json
import random

@dataclass
class Word:
    en: str
    ko: str

class WordBook:
    def __init__(self, path: Path):
        self.path = path
        self.words: list[Word] = self._load()

    def _load(self):
        if not self.path.exists():
            return []
        data = json.loads(self.path.read_text(encoding="utf-8"))
        return [Word(**d) for d in data]

    def save(self):
        data = [asdict(w) for w in self.words]
        self.path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def add(self, en, ko):
        self.words.append(Word(en, ko))
        self.save()

    def remove(self, en):
        before = len(self.words)
        self.words = [w for w in self.words if w.en != en]
        self.save()
        return before - len(self.words) > 0

    def quiz(self, count=5):
        if not self.words:
            return 0, 0
        score = 0
        questions = random.sample(self.words, min(count, len(self.words)))
        for i, w in enumerate(questions, 1):
            ans = input(f"[{i}/{len(questions)}] {w.en}? ").strip()
            if ans == w.ko:
                print("정답!")
                score += 1
            else:
                print(f"오답. 정답: {w.ko}")
        return score, len(questions)
