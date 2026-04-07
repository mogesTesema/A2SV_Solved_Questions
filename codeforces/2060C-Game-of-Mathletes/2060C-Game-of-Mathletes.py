def mathlets():
    n,k = map(int, input().split())
    integers = list(map(int, input().split()))
    integers.sort()
    score = 0
    left = 0
    right = n - 1
    while(left < right):
        temp = integers[left] + integers[right]
        if temp > k:
            right -= 1
        elif temp < k:
            left += 1
        else:
            score += 1
            left += 1
            right -= 1
    print(score)
test = int(input())
for _ in range(test):
    mathlets()