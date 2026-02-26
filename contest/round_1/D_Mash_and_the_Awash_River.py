import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        s = data[i]
        if "><" in s or "**" in s or ">*" in s or "*<" in s:
            results.append("-1")
        else:
            lc = s.count('<')
            rc = s.count('>')
            if '*' in s:
                results.append(str(max(lc + 1, rc + 1)))
            else:
                results.append(str(max(lc, rc)))
    
    sys.stdout.write("\n".join(results) + "\n")


solve()