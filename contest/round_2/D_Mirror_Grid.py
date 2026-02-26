t = int(input())
for _ in range(t):
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    ans = 0

    for i in range(n // 2):
        for j in range((n + 1) // 2):
            cells = [
                grid[i][j],
                grid[j][n - 1 - i],
                grid[n - 1 - i][n - 1 - j],
                grid[n - 1 - j][i]
            ]
            ones = cells.count('1')
            ans += min(ones, 4 - ones)

    print(ans)