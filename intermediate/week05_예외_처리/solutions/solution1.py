def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("정수만 입력하세요")

n = read_int("나이를 입력하세요: ")
print(f"나이: {n}")
