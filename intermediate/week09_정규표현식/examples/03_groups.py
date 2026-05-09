import re

log = "ERROR 2026-05-09 14:32 사용자 인증 실패"

m = re.match(r"(\w+) (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) (.+)", log)
print(m.groups())
print(m.group(1), m.group(2))

# 명명 그룹
m = re.match(
    r"(?P<level>\w+) (?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}) (?P<msg>.+)",
    log,
)
print(m.group("level"))
print(m.group("date"))
print(m.groupdict())
