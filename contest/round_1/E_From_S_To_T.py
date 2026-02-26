from collections import Counter
 
def solve():
    s = input().strip()
    t = input().strip()
    p = input().strip()
    
   
    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1
    if i != len(s):
        print("NO")
        return
    
    
    cs = Counter(s)
    ct = Counter(t)
    cp = Counter(p)
    
    for ch in ct:
        if ct[ch] > cs.get(ch, 0) + cp.get(ch, 0):
            print("NO")
            return
    
    print("YES")
 
 
q = int(input())
for _ in range(q):
    solve()