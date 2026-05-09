import re

# 검색 (첫 매치만)
m = re.search(r"\d{3}-\d{4}-\d{4}", "전화번호: 010-1234-5678 입니다")
print(m.group())

# 모두 찾기
print(re.findall(r"\d+", "사과 5개, 바나나 3개, 포도 12개"))

# 매치 여부 (처음부터 매치)
if re.match(r"^\d+$", "12345"):
    print("숫자만으로 구성")

# 매치 결과 정보
m = re.search(r"hello", "say hello world")
print(m.start(), m.end(), m.span())
