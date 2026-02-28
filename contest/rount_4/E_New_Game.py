from collections import Counter
def solve():
    n , k = map(int,input().split())
    nums = list(map(int,input().split()))

    numc = Counter(nums)
    sorted = numc.most_common()
    print(sorted)


t = int(input())
for _ in range(t):
    solve()