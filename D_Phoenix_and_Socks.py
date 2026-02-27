from collections import Counter

def solve():
    t = int(input())
    for _ in range(t):
        n, l, r = map(int, input().split())
        socks = list(map(int, input().split()))

        left = Counter(socks[:l])
        right = Counter(socks[l:])

        for color in list(left.keys()):
            matched = min(left[color], right.get(color, 0))
            left[color] -= matched
            right[color] -= matched
            l -= matched
            r -= matched

        if l < r:
            left, right = right, left
            l, r = r, l

        diff = (l - r) // 2

        same_side_pairs = 0
        for color in left:
            same_side_pairs += left[color] // 2

        p = min(diff, same_side_pairs)

        print(l - p)


solve()