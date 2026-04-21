# example below, replace it with your solution
from collections import defaultdict
n,m = map(int,input().split())

adj_list = defaultdict(list)

for i in range(m):
    x,y = map(int,input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

degree = None

for key, nodes in adj_list.items():
    if degree == None:
        degree == len(nodes)
        continue
    if len(nodes) != degree:
        print("NO")
        break
print("YES")