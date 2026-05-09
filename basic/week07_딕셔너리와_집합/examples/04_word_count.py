text = "apple banana apple grape banana apple"
words = text.split()

count = {}
for word in words:
    count[word] = count.get(word, 0) + 1

print(count)
# {'apple': 3, 'banana': 2, 'grape': 1}
