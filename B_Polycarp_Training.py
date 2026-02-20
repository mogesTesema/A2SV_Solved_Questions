n = int(input())
contests = list(int(x) for x in input().split())
contests.sort()
day = 0
k = 1
index = 0
while index < len(contests):
    val = contests[index]
    if val >= k:
        day +=1
        index += 1
    else:
        while index < len(contests) and contests[index]< k:
            index += 1
        if index < len(contests) and contests[index]>= k:
            day +=1
            index += 1

        
    k += 1
print(day)
