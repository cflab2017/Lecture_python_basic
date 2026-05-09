import json

data = {
    "name": "홍길동",
    "age": 20,
    "skills": ["Python", "SQL", "Git"],
    "active": True,
    "address": {"city": "서울", "zip": "12345"},
}

# 저장
with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 로드
with open("profile.json", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["name"])
print(loaded["skills"])
print(loaded["address"]["city"])

# 문자열로 직접
s = json.dumps(data, ensure_ascii=False)
print(s[:50], "...")

import os
os.remove("profile.json")
