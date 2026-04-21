# example below, replace it with your solution
from collections import defaultdict
n = int(input())
k = int(input())
graph = defaultdict(list)
for i in range(k):
    command = list(map(int,input().split()))
    if len(command) == 3:
        graph[command[1]].append(command[2])
        graph[command[2]].append(command[1])
    else:
        if len(graph[command[1]]) == 0:
            print("")
        else:
            print(" ".join(str(x) for x in graph[command[1]]))