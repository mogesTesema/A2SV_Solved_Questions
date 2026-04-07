wires =int(input())
oskals = list(map(int, input().split(" ")))
shoots = int(input())
for i in range(shoots):
    x, y = map(int,input().split(" "))
    x = x-1
    if wires == 1:
        oskals[0] = 0
    elif  x ==0:
        oskals[x+1] += oskals[x]-y
        oskals[x]  = 0
        
    elif x == wires -1:
        oskals[x-1] += y-1
        oskals[x]  = 0
        
    else:
       
        oskals[x+1] += oskals[x]-y
        oskals[x-1] += y-1
        oskals[x]  = 0
for i in oskals:
    print(i)