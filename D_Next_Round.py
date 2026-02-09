n, k = [int(i)for i in input().split()]
contestan = [int(x)for x in input().split()]
selected = 0
for i in range(n):
    if contestan[i] >0 and contestan[i] >= contestan[k-1]:
        selected += 1
    else:
        break
print(selected)

