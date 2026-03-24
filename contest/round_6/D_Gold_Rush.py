def solve():
    n,m = map(int,input().split())
    
    def recurse(x):
        if x == m:
            return True
            

        
        if x < m or x % 3 != 0:
            return False
        
        return recurse(x//3) or recurse(2*x//3)
    
    print("YES" if recurse(n) else "NO")

t = int(input())
for _ in range(t):
    solve()