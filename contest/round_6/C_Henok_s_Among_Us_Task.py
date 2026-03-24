import sys
def solve():
    a,b = map(int,input().split())
    flag = False
    def recurse(a,arr):
        arr = arr[::]
        if a == b:
            print("YES")
            print(len(arr))
            print(' '.join(list(str(x) for x in arr)))
            sys.exit()
            return True
        if a > b:
            return False
        
        first = arr[::]
        second = arr[::]
        first.append(a*2)
        second.append(a*10+1)
        flag = recurse(a*2,first) or recurse(a*10+1,second)
        return flag
    l = list([a])
    ans = recurse(a,l)
    if not ans:
        print("NO")
      

solve()