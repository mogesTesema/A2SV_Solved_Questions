def solve():
    n = int(input())
    a = list(map(int, input().split()))

    totalSum = 0
    i = 0
    while i < n:
        currentSign = a[i] > 0
        
        currentMax = a[i]
        j = i + 1
        while j < n:
            if (a[j] > 0) == currentSign:
                currentMax = max(currentMax, a[j])
            else:
                break
            j += 1
        totalSum += currentMax
        i = j
    print(totalSum)

t = int(input())
for _ in range(t):
    solve()