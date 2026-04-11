t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    pr = [0]
    for x in r:
        pr.append(pr[-1] + x)
    
    pb = [0]
    for x in b:
        pb.append(pb[-1] + x)
    
    best_r = max(pr)
    best_b = max(pb)
    
    ans = 0
    for i in range(n + 1):
        for j in range(m + 1):
            ans = max(ans, pr[i] + pb[j])
    
    print(max(0, ans))