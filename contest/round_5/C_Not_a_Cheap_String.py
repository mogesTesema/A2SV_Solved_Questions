t = int(input())

for _ in range(t):
    w = input().strip()
    p = int(input())
    a = [0]*27
    s = 0
    for c in w:
        v = ord(c)-96
        a[v] += 1
        s += v

    r = [0]*27
    for i in range(26,0,-1):
        while a[i]>0 and s >p:
            a[i] -= 1
            r[i] += 1
            s -= i
    ans = []
    for c in w:
        v = ord(c)-96
        if r[v] > 0:
            r[v] -= 1
        else:
            ans.append(c)
    print("".join(ans))