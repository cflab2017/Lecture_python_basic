height = int(input("높이: "))

print("[정삼각형]")
for i in range(1, height + 1):
    print("*" * i)

print()
print("[역삼각형]")
for i in range(height, 0, -1):
    print("*" * i)
