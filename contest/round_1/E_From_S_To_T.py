from collections import Counter
def solve():
    s = list(input())
    t = list(input())
    p = list(input())

    s = Counter(s)
    t = Counter(t)
    p = Counter(p)
    for item in t:
        if t[item] > p.get(item,0) + t.get(item,0):
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()




