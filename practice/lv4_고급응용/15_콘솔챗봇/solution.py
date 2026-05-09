"""규칙 기반 콘솔 챗봇 — API 키 없이 동작"""
import json
import re
from pathlib import Path
from datetime import datetime

HISTORY = Path("chat_history.json")

RULES = [
    (r"안녕|hello|hi", "안녕하세요!"),
    (r"이름|누구", "저는 학습용 챗봇입니다."),
    (r"날씨", "죄송해요, 실시간 날씨는 못 알려드려요."),
    (r"파이썬|python", "파이썬은 1991년에 발표된 인터프리터 언어예요."),
    (r"감사|고마워|thanks", "천만에요!"),
    (r"(\d+)\s*\+\s*(\d+)", lambda m: f"= {int(m.group(1)) + int(m.group(2))}"),
]

def respond(text):
    for pattern, reply in RULES:
        m = re.search(pattern, text)
        if m:
            return reply(m) if callable(reply) else reply
    return "잘 모르겠어요. 다시 말씀해주세요."

def save(history):
    HISTORY.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")

def load():
    return json.loads(HISTORY.read_text(encoding="utf-8")) if HISTORY.exists() else []

def main():
    history = []
    print("챗봇 시작 (/quit 으로 종료, /help 로 명령어)")
    while True:
        user = input("\nyou: ").strip()
        if not user: continue
        if user.startswith("/"):
            cmd = user[1:]
            if cmd in ("quit", "exit"): break
            elif cmd == "help":
                print("/clear /save /load /history /quit")
            elif cmd == "clear": history = []; print("이력 초기화")
            elif cmd == "save": save(history); print("저장됨")
            elif cmd == "load": history = load(); print(f"불러옴 ({len(history)}개)")
            elif cmd == "history":
                for h in history[-5:]:
                    print(f"  [{h['time']}] {h['who']}: {h['text']}")
            continue
        bot_reply = respond(user)
        ts = datetime.now().strftime("%H:%M:%S")
        history.append({"time": ts, "who": "user", "text": user})
        history.append({"time": ts, "who": "bot", "text": bot_reply})
        print(f"bot: {bot_reply}")

if __name__ == "__main__":
    main()
