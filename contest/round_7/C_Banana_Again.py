n = int(input())
bana = list(map(int,input().split()))
glob_min = float('inf')
total= sum(bana)
def backtrack(index, g1):
    global glob_min
    if index == n:
        g2 = total - g1
        glob_min = min(glob_min, abs(g1 - g2))
        return
    
    backtrack(index + 1, g1 + bana[index])
    
    backtrack(index + 1, g1)

backtrack(0, 0)
print(glob_min)
        



    