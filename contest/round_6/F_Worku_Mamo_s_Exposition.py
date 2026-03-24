import sys
from collections import deque

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    h = list(map(int, input_data[2:]))
    
    min_q = deque()
    max_q = deque()
    
    left = 0
    max_len = 0
    results = []
    
    for right in range(n):
        # Maintain Min-Deque: remove elements larger than current height
        while min_q and h[min_q[-1]] >= h[right]:
            min_q.pop()
        min_q.append(right)
        
        # Maintain Max-Deque: remove elements smaller than current height
        while max_q and h[max_q[-1]] <= h[right]:
            max_q.pop()
        max_q.append(right)
        
        # Shrink window from the left if the difference exceeds k
        while h[max_q[0]] - h[min_q[0]] > k:
            left += 1
            if min_q[0] < left:
                min_q.popleft()
            if max_q[0] < left:
                max_q.popleft()
        
        current_len = right - left + 1
        
        if current_len > max_len:
            max_len = current_len
            results = [(left + 1, right + 1)]
        elif current_len == max_len:
            results.append((left + 1, right + 1))
            
    # Output results
    print(f"{max_len} {len(results)}")
    for res in results:
        print(f"{res[0]} {res[1]}")

if __name__ == "__main__":
    solve()