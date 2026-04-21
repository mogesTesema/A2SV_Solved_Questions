def _norm(num_str):
    stripped = num_str.lstrip("0")
    return stripped if stripped else "0"


def _less_than(a, b):
    a = _norm(a)
    b = _norm(b)
    if len(a) != len(b):
        return len(a) < len(b)
    return a < b


def solve():
    q = int(input())
    for _ in range(q):
        n = int(input())
        s = input().strip()
        found = False
        for i in range(1, n):
            a = s[:i]
            b = s[i:]
            if _less_than(a, b):
                print("YES")
                print(2)
                print(a, b)
                found = True
                break
        if not found:
            print("NO")

solve()