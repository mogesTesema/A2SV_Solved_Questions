def solve():
    k = int(input())
    finalist = list(map(int,input().split()))

    large = max(finalist)
    if large <= 25:
        print(0)
    else:
        print(large-25)


solve()