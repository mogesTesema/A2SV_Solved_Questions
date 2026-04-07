def teacher():
    n, m, q = list(map(int,input().split(" ")))
    teachers = list(map(int,input().split()))
    devinCell = int(input())
    teacher1 = teachers[0]
    teacher2 = teachers[1]
    maxs = max(teacher1,teacher2)
    mins = min(teacher1,teacher2)
    
    if devinCell < mins:
        print(mins-1)
        return
    elif devinCell > maxs:
        print(n - maxs)
        return
    elif devinCell == mins or devinCell == maxs:
        print(0)
        return
    else:
        print((maxs-mins)//2)
        
test = int(input())
for i in range(test):
    teacher()