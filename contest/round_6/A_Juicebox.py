import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    results = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        k = int(input_data[ptr + 1])
        ptr += 2
        

        brand_totals_map = {}
        for _ in range(k):
            b = input_data[ptr]
            c = int(input_data[ptr + 1])
            brand_totals_map[b] = brand_totals_map.get(b, 0) + c
            ptr += 2
      
        heap = [-v for v in brand_totals_map.values()]
        heapq.heapify(heap)
        
        total_profit = 0
       
        for _ in range(min(n, len(heap))):
            total_profit += -heapq.heappop(heap)
            
        results.append(str(total_profit))
    
    sys.stdout.write("\n".join(results) + "\n")


solve()