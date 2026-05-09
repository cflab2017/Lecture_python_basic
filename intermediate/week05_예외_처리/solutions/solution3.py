path = input("경로: ").strip()

try:
    with open(path, encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"파일 없음: {path}")
except PermissionError:
    print(f"권한 없음: {path}")
except UnicodeDecodeError:
    print(f"인코딩 오류: {path}")
except OSError as e:
    print(f"기타 OS 에러: {e}")
