def digitSum():
    x,y = list(map(int,input().split()))
    if (x+1-y)/9 >= 0 and (x+1-y)%9 == 0:
        print("YES")
    else:
        print("NO")
test = int(input())
for i in range(test):
    digitSum()