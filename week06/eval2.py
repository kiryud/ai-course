import contextlib
import io
import re
import sys
from openai import OpenAI

client = OpenAI(base_url="https://krchoi.com/gemma4/v1", api_key="none")
MODEL = "gemma4"
N = 5

TESTS = [
    ("1234000", "1234000"),
    ("1,234,000", "1234000"),
    ("123만 4천원", "1234000"),
    ("1,234,000원", "1234000"),
    ("1234000원", "1234000"),
    ("8,445,120,050", "8445120050"),
    ("8,445,120,050원", "8445120050"),
    ("8445120050원", "8445120050"),
    ("5만 33천원", None),
    ("1574145래", None),
    ("1,574,14532", None),
    ("12,1574145", None),
    ("1665,648,645,156원", None),
    ("", None),
]


def generate(prompt):
    r = client.chat.completions.create(
        model=MODEL, temperature=0.7, max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )
    return r.choices[0].message.content


def extract_code(text):
    blocks = re.findall(r"```(?:python)?\n(.*?)```", text, re.S)
    return blocks[0] if blocks else text


def score(code):
    space = {}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(code, space)
    except Exception as e:
        return 0, f"실행 오류: {e}"
    func = space.get("parse_won")
    if func is None:
        names = [k for k, v in space.items() if callable(v) and not k.startswith("_")]
        return 0, f"parse_won 없음. 있는 함수: {names}"
    passed, failed = 0, []
    for arg, want in TESTS:
        try:
            got = func(arg)
        except Exception as e:
            got = f"예외 {type(e).__name__}"
        if got == want:
            passed += 1
        else:
            failed.append(f"{arg!r} -> {got!r}")
    return passed, "; ".join(failed)


prompt = open(sys.argv[1], encoding="utf-8").read()
total = 0
for i in range(N):
    code = extract_code(generate(prompt))
    open(f"out_{i + 1}.py", "w", encoding="utf-8").write(code)
    passed, note = score(code)
    total += passed
    print(f"{i + 1}회: {passed}/{len(TESTS)}  {note}")
print(f"평균 {total / N:.1f}/{len(TESTS)}")
