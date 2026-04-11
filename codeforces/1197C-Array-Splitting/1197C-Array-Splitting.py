import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

gaps = []
for i in range(1, n):
    gaps.append(a[i] - a[i-1])

gaps.sort(reverse=True)

ans = a[-1] - a[0]
for i in range(k-1):
    ans -= gaps[i]

print(ans)