# example below, replace it with your solution
from collections import defaultdict
n = int(input())
adj_list = defaultdict(list)
graph = [[0]*n for _ in range(n)]
for i in range(n):
    adj = list(map(int,input().split()))
    if len(adj) <= 1:
        continue
    x, nums = adj[0],adj[1:]
    for a in range(x):
        graph[i][nums[a]-1] = 1
    
for g in graph:
    print(" ".join(str(x) for x in g))