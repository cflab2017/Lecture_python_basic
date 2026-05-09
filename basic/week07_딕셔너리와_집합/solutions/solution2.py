text = "apple banana apple cherry banana apple cherry apple banana apple cherry banana apple"

count = {}
for word in text.split():
    count[word] = count.get(word, 0) + 1

# 빈도 내림차순으로 정렬
top3 = sorted(count.items(), key=lambda x: -x[1])[:3]
for i, (word, c) in enumerate(top3, 1):
    print(f"{i}. {word}: {c}번")
