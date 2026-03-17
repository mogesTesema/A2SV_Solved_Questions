t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    if n == 1 and m == 1:
        print(-1)
    elif n == 1:
        print(*a[0][1:], a[0][0])
    elif m == 1:
        for i in range(n):
            print(a[(i+1)%n][0])
    else:
        for i in range(n):
            print(*a[i][1:], a[i][0])