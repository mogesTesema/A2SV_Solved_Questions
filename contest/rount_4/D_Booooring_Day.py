def solve():
    n,l,r = map(int,input().split())
    cards = list(map(int,input().split()))
    win = 0
    if n == 0:
        print(0)
        return

    def between(x):
        return l <= x <= r
    prev = 0
    for right in range(len(cards)):
        if between(cards[right]):
            win += 1
            prev = 0
        elif cards[right] > r:
            prev = 0
        elif cards[right] < l:
            curr = cards[right]+prev
            if between(curr):
                win += 1
                prev = 0
            elif curr < l:
                prev = curr
            elif curr > r:
                prev = 0

    print(win)

t = int(input())

for _ in range(t):
    solve()

