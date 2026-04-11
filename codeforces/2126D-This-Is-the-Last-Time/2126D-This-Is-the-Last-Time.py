import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    casinos = [tuple(map(int, input().split())) for _ in range(n)]
    casinos.sort()
    
    import heapq
    pq = []
    i = 0
    
    while True:
        while i < n and casinos[i][0] <= k:
            l, r, real = casinos[i]
            heapq.heappush(pq, (-real, r))
            i += 1
        
        updated = False
        while pq:
            real, r = heapq.heappop(pq)
            real = -real
            if k <= r:
                if real > k:
                    k = real
                    updated = True
                break
        
        if not updated:
            break
    
    print(k)