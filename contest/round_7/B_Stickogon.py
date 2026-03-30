from collections import defaultdict
def solve():
    poly = 0
    n = int(input())
    sticks = list(map(int,input().split()))

    stick_freq = defaultdict()

    for stick in sticks:
        stick_freq[stick] = stick_freq.get(stick,0) + 1

    for key, val in stick_freq.items():
        if val >= 3:
            n = val // 3
            poly += n

    print(poly)

t = int(input())

for _ in range(t):
    solve()