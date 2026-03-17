def solve():
    line = input().split()
    if not line:
        return
    n = int(line[0])
    s = input().strip()
    
    if n == 1:
        print("Yes")
    elif len(set(s)) < n:
        print("Yes")
    else:
        print("No")


solve()