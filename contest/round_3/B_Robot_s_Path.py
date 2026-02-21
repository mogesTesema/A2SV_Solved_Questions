n,k = [int(x) for x in input().split()]
obs = input().split(".")
lens = []
for ob in obs:
    lens.append(len(ob))
max_ob = max(lens)
if max_ob >= k:
    print("NO")
else:
    print("YES")