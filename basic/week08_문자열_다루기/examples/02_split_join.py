csv = "사과,바나나,포도"
fruits = csv.split(",")
print(fruits)

joined = " | ".join(fruits)
print(joined)

# 공백으로 분리
s = "Hello   World    Python"
print(s.split())   # ['Hello', 'World', 'Python']

# 줄바꿈으로 분리
text = "1줄\n2줄\n3줄"
print(text.splitlines())
