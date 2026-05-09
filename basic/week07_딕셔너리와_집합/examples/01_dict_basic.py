student = {"name": "홍길동", "age": 20, "major": "CS"}

print(student["name"])
print(student["age"])

student["age"] = 21
student["email"] = "hong@example.com"
print(student)

del student["major"]
print(student)
