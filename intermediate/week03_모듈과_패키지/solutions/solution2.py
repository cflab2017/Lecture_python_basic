"""문자열 유틸리티 함수 모음"""

def slugify(text):
    return text.strip().lower().replace(" ", "-")

def truncate(text, max_len):
    if len(text) <= max_len:
        return text
    return text[:max_len - 3] + "..."

def wrap(text, width):
    return "\n".join(text[i:i+width] for i in range(0, len(text), width))

if __name__ == "__main__":
    print(slugify(" Hello World "))
    print(truncate("이 문장은 길어요", 5))
    print(wrap("abcdefghij", 4))
