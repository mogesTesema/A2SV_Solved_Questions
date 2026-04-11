import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    ans = float('inf')
    for i in range(n):
        a = b = c = 0
        for j in range(i, min(n, i + 7)):
            if s[j] == 'a':
                a += 1
            elif s[j] == 'b':
                b += 1
            else:
                c += 1
            if j - i + 1 >= 2 and a > b and a > c:
                ans = min(ans, j - i + 1)
    print(ans if ans != float('inf') else -1)