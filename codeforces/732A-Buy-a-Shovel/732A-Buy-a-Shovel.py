k, r  = list(map(int,input().split()))

iterate =1
while True:
    if k * iterate % 10 == 0:
        break
    elif (k * iterate) % 10== r:
        break
    iterate +=1
print(iterate)