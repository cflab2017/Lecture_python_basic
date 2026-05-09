text = input("문장: ")

char_count = len(text.replace(" ", ""))
words = text.split()
word_count = len(words)
avg_len = sum(len(w) for w in words) / word_count if word_count else 0

print(f"\n글자 수(공백 제외): {char_count}")
print(f"단어 수: {word_count}")
print(f"평균 단어 길이: {avg_len:.2f}")
