"""텍스트 어드벤처 — 분기 + HP"""
import json
from pathlib import Path

# 시나리오를 인라인으로 (실제로는 JSON 파일에서)
SCENES = {
    "start": {
        "text": "어두운 숲에 들어섰다. 길은 둘로 갈라진다.",
        "choices": {
            "1": {"label": "왼쪽으로", "next": "left", "effect": {"hp": 0}},
            "2": {"label": "오른쪽으로", "next": "right", "effect": {"hp": 0}},
        },
    },
    "left": {
        "text": "늑대를 만났다! 싸울까 도망갈까?",
        "choices": {
            "1": {"label": "싸운다", "next": "fight", "effect": {"hp": -30}},
            "2": {"label": "도망친다", "next": "escape", "effect": {"hp": -10}},
        },
    },
    "right": {
        "text": "낡은 오두막을 발견. 들어갈까?",
        "choices": {
            "1": {"label": "들어간다", "next": "treasure", "effect": {"hp": 0, "item": "검"}},
            "2": {"label": "지나친다", "next": "lost", "effect": {"hp": 0}},
        },
    },
    "fight": {"text": "늑대를 물리치고 보물 발견! 🏆", "ending": True, "result": "GOOD"},
    "escape": {"text": "안전하게 마을로. 평범한 결말.", "ending": True, "result": "NEUTRAL"},
    "treasure": {"text": "오두막에서 검을 얻고 영웅이 됨! 🏆", "ending": True, "result": "GOOD"},
    "lost": {"text": "숲에서 길을 잃고 사라짐...", "ending": True, "result": "BAD"},
}

def main():
    state = {"hp": 100, "items": []}
    current = "start"
    while True:
        scene = SCENES[current]
        print(f"\n{scene['text']}")
        print(f"[HP: {state['hp']}, 아이템: {state['items']}]")

        if scene.get("ending"):
            print(f"\n=== 엔딩: {scene['result']} ===")
            break

        for k, ch in scene["choices"].items():
            print(f"  {k}. {ch['label']}")
        pick = input("> ").strip()
        if pick not in scene["choices"]:
            print("잘못된 선택"); continue

        choice = scene["choices"][pick]
        effect = choice.get("effect", {})
        state["hp"] += effect.get("hp", 0)
        if "item" in effect:
            state["items"].append(effect["item"])
        if state["hp"] <= 0:
            print("\n=== HP 0! 게임 오버 ===")
            break
        current = choice["next"]

if __name__ == "__main__":
    main()
