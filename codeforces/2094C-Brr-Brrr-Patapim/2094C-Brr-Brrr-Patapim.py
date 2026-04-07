import sys

def solve():
    n = int(sys.stdin.readline())
    grid = []
    present = [False] * (2 * n + 1)
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append(row)
        for x in row:
            present[x] = True

    p1 = -1
    for i in range(1, 2 * n + 1):
        if not present[i]:
            p1 = i
            break

    permutation = [p1] + grid[0] + [grid[i][n - 1] for i in range(1, n)]
    sys.stdout.write(' '.join(map(str, permutation)) + '\n')

t = int(sys.stdin.readline())
for _ in range(t):
    solve()