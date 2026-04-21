# example below, replace it with your solution
n = int(input())
graph_grid = [list(map(int,input().split())) for x in range(n)]
visited = set()
counter = 0
for i in range(n):
    is_visited = False
    for j in range(n):
        if graph_grid[i][j] == 1:
            if j not in visited:
                counter += 1
                is_visited = True
    if is_visited:
        visited.add(i)
print(int(counter))