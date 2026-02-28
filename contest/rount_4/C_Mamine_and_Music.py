n,k = map(int,input().split())
days = list(map(int,input().split()))
days = [[x,i+1] for i,x in enumerate(days)]
days.sort()

inst = 0
total = 0
i = 0
index = []
while total < k and i < len(days):
    total += days[i][0]
    if total <= k:
        index.append(days[i][1])
        inst += 1
        i+= 1
    else:
        break

print(inst)
print(" ".join([str(x) for x in index]))