import itertools as it

LOG = """2026-05-09 10:00 INFO 시작
2026-05-09 10:05 ERROR 에러
2026-05-10 09:00 INFO 시작
2026-05-10 11:00 INFO 정상""".splitlines()

def date_of(line):
    return line.split(" ", 1)[0]

# 정렬된 가정. groupby 는 연속된 같은 키만 묶음
for date, group in it.groupby(LOG, key=date_of):
    print(f"[{date}]")
    for line in group:
        print(f"  {line[len(date)+1:]}")
