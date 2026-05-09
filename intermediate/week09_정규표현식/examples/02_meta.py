import re

text = "abc123 XYZ 가나다 ___ "

print(re.findall(r"\d", text))      # 숫자
print(re.findall(r"\w+", text))     # 단어 (숫자/알파벳/언더스코어/유니코드)
print(re.findall(r"\s+", text))     # 공백
print(re.findall(r"[A-Z]+", text))  # 대문자
print(re.findall(r"[가-힣]+", text)) # 한글
print(re.findall(r"^\w+", text))    # 시작
print(re.findall(r"\w+$", text))    # 끝 (양 끝 공백 제거 안 됐으므로 빈 결과)
