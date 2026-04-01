def solve():

    q = input()
    n = len(q)
    x = int(input())
    ks = list(map(int,input().split()))
    ans = ""
    for k in ks:
        block = (k-1)/n
        remain = (k-1) % n

        if block % 2 == 0:
            print(q[remain])
        else:
            a = q[remain]
            a.swapcase()
            print(a)

t = int(input())

for _ in range(t):
    solve()