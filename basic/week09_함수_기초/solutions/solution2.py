def is_valid_age(value):
    if not isinstance(value, int):
        return False
    return 0 <= value <= 120

# 테스트
print(is_valid_age(20))
print(is_valid_age(0))
print(is_valid_age(120))
print(is_valid_age(-1))
print(is_valid_age(150))
print(is_valid_age("abc"))
