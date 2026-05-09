s = "  Hello, Python!  "

print(s.strip())                   # "Hello, Python!"
print(s.lower())                   # "  hello, python!  "
print(s.upper())                   # "  HELLO, PYTHON!  "
print(s.replace("Python", "World"))
print(s.find("Python"))            # 9
print(s.count("l"))                # 3
print(s.startswith("  H"))         # True
print(s.endswith("!  "))           # True
print("123".isdigit())             # True
print("abc".isalpha())             # True
