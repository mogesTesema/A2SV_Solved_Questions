# example below, replace it with your solution
from collections import defaultdict


n = int(input())
adjacency_list = defaultdict(list)

for i in range(n):
    cols = list(map(int,input().split()))
    for index, col in enumerate(cols):
        if col == 1:
            adjacency_list[i+1].append(index+1)

for node, adj in adjacency_list.items():
    adj.sort()
    print(" ".join([str(len(adj))]+[str(x) for x in adj]))