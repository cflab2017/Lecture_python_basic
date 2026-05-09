import re

LOG = """
INFO 2026-05-09 10:00 시작
ERROR 2026-05-09 10:05 인증 실패
WARN 2026-05-09 10:07 느림
ERROR 2026-05-09 10:30 DB 연결 끊김
INFO 2026-05-09 10:35 재시작
"""

pattern = re.compile(r"^ERROR \d{4}-\d{2}-\d{2} (\d{2}:\d{2})", re.MULTILINE)
for time in pattern.findall(LOG):
    print(f"[ERROR] {time}")
