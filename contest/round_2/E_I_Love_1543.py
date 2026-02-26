t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    total = 0
    layers = min(n, m) // 2

    for layer in range(layers):
        top = layer
        bottom = n - 1 - layer
        left = layer
        right = m - 1 - layer

        path = []

        for j in range(left, right + 1):
            path.append(grid[top][j])
        for i in range(top + 1, bottom + 1):
            path.append(grid[i][right])
        for j in range(right - 1, left - 1, -1):
            path.append(grid[bottom][j])
        for i in range(bottom - 1, top, -1):
            path.append(grid[i][left])

        s = ''.join(path)
        s += s[:3]

        for i in range(len(path)):
            if s[i:i+4] == "1543":
                total += 1

    print(total)