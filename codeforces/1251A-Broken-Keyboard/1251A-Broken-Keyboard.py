t = int(input())
for _ in range(t):
    s = input().strip()
    i = 0
    res = set()
    n = len(s)
    while i < n:
        if i + 1 < n and s[i] == s[i + 1]:
            i += 2
        else:
            res.add(s[i])
            i += 1
    print("".join(sorted(res)))