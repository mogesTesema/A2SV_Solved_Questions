from collections import Counter

def solve():
    n, k = map(int,input().split())
    nums = list(map(int,input().split()))

    num_freq = Counter(nums)

    for val in num_freq.values():
        if val > k:
            print("NO")
            return

    indexed = [(num, i) for i, num in enumerate(nums)]
    indexed.sort()

    ans = [0] * n
    color = 1
    print(indexed)
    for _, idx in indexed:
        ans[idx] = color
        color += 1
        if color > k:
            color = 1

    print("YES")
    print(" ".join(str(x) for x in ans))


solve()

