import sys
input = sys.stdin.readline

h, w = map(int, input().split())
g = [input().strip() for _ in range(h)]

hor = [[0] * w for _ in range(h)]
ver = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w - 1):
        hor[i][j] = (g[i][j] == '.' and g[i][j + 1] == '.')

for i in range(h - 1):
    for j in range(w):
        ver[i][j] = (g[i][j] == '.' and g[i + 1][j] == '.')

for i in range(h):
    for j in range(w):
        hor[i][j] += hor[i][j - 1] if j else 0

for j in range(w):
    for i in range(h):
        ver[i][j] += ver[i - 1][j] if i else 0

hor_ps = [[0] * w for _ in range(h)]
ver_ps = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        hor_ps[i][j] = hor[i][j] + (hor_ps[i - 1][j] if i else 0)

for j in range(w):
    for i in range(h):
        ver_ps[i][j] = ver[i][j] + (ver_ps[i][j - 1] if j else 0)

for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1
    
    ans = 0
    
    for i in range(r1, r2 + 1):
        if c1 < c2:
            ans += hor[i][c2 - 1] - (hor[i][c1 - 1] if c1 else 0)
    
    for j in range(c1, c2 + 1):
        if r1 < r2:
            ans += ver[r2 - 1][j] - (ver[r1 - 1][j] if r1 else 0)
    
    print(ans)