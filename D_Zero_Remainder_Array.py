t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split]
    cnt2 = 0
    cnt3 = 0
    while n % 2 == 0:
        n //= 2
        cnt2 += 1
    while n % 3 == 0:
        n //= 3
        cnt3 += 1
    if n == 1 and cnt2 <= cnt3:
        print(2 * cnt3 - cnt2)
    else:
        print(-1)