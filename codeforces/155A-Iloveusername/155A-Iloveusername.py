n = int(input())
points = list(map(int,input().split()))
amazing = 0
if n != 0:
    max = points[0]
    min = points[0]
for i in range(1,n):
    if points[i] > max:
        amazing += 1
        max = points[i]
    elif points[i] < min:
        amazing +=1
        min = points[i]
print( amazing)