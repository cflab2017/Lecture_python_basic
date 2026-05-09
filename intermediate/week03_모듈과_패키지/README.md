# 3주차. 모듈과 패키지

> 단계: 중급 | 선수: 2주차

## 학습 목표
- 자체 모듈을 만들고 import한다
- `__name__ == "__main__"` 패턴을 안다
- 패키지 구조와 `__init__.py` 의 역할을 이해한다
- `pip` 으로 외부 패키지를 설치한다

## 1. 모듈

`.py` 파일이 곧 모듈. import로 다른 파일에서 사용.

```python
# calc.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```

```python
# main.py
import calc
print(calc.add(3, 5))

from calc import add, sub
print(add(1, 2), sub(5, 3))

from calc import add as plus
print(plus(10, 20))
```

## 2. `__name__ == "__main__"`

스크립트로 직접 실행될 때만 동작하는 코드.

```python
# mymod.py
def main():
    print("실행됨")

if __name__ == "__main__":
    main()
```

이 패턴 덕분에 `import mymod` 해도 `main()` 이 자동 실행되지 않음.

## 3. 패키지

폴더에 여러 모듈을 묶은 것. `__init__.py` 가 있어야 패키지로 인식 (Python 3.3+ 부터 없어도 됨).

```
mypkg/
├── __init__.py
├── math_utils.py
└── string_utils.py
```

```python
# 사용
from mypkg.math_utils import add
from mypkg.string_utils import slugify
```

## 4. `__init__.py` 활용

```python
# mypkg/__init__.py
from .math_utils import add, sub
from .string_utils import slugify
```

이렇게 하면 `from mypkg import add` 가능 (간편).

## 5. pip 으로 외부 패키지 설치

```bash
pip install requests
pip install requests==2.31.0       # 특정 버전
pip install -r requirements.txt    # 일괄 설치
pip list                            # 설치된 목록
```

## 핵심 예제 (examples/)

| 파일 | 다루는 내용 |
|------|------------|
| `calc.py` | 자체 모듈 |
| `main.py` | calc 모듈 import 사용 |
| `mypkg/__init__.py`, `math_utils.py`, `string_utils.py` | 패키지 |
| `use_pkg.py` | 패키지 사용 |

## ⚠️ 자주 하는 실수

1. **순환 import** — A가 B를, B가 A를 import → ImportError
2. **상대 import 잘못** — 패키지 내부에서는 `from .module import ...`
3. **모듈 이름이 표준 라이브러리와 충돌** — `random.py` 라는 파일을 만들면 표준 random이 가려짐

## ❓ FAQ

**Q1. `import` 와 `from` 중 뭘 쓰나요?**
A. 사용하는 함수가 1-2개면 `from`, 많거나 모듈 이름을 명시하고 싶으면 `import`.

**Q2. `pip` 가 안 깔려있어요**
A. `python -m ensurepip` 또는 `python -m pip --version` 으로 확인.

**Q3. 가상환경(venv)은 왜 쓰나요?**
A. 프로젝트마다 라이브러리 버전을 분리. 다음 학기·실무에서 거의 필수.

## 📝 과제 (exercises/)

- `exercise1.md` — `calculator/` 패키지 (basic + advanced)
- `exercise2.md` — `string_utils.py` (slugify, truncate)
- `exercise3.md` — `__name__ == "__main__"` 활용

## 다음 주차

[4주차. 표준 라이브러리](../week04_표준_라이브러리/)
