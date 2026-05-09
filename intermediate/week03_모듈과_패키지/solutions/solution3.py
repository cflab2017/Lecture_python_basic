"""greet.py — 라이브러리 + 스크립트 양쪽으로 사용 가능"""

def greet(name):
    return f"안녕, {name}!"

if __name__ == "__main__":
    name = input("이름: ").strip()
    print(greet(name))
