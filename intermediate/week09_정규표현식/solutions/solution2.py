import re

PATTERN = re.compile(r"^010-\d{4}-\d{4}$")

def is_valid_phone(s):
    return bool(PATTERN.match(s))

print(is_valid_phone("010-1234-5678"))   # True
print(is_valid_phone("011-1234-5678"))   # False
print(is_valid_phone("010 1234 5678"))   # False
print(is_valid_phone("010-12345-678"))   # False
print(is_valid_phone("01012345678"))     # False
