def solve():
        n, l, r = map(int, input().split())
        cards = list(map(int, input().split()))
        
        wins = 0
        current_sum = 0
        left = 0
        
        for right in range(n):
            current_sum += cards[right]
            
            while current_sum > r and left <= right:
                current_sum -= cards[left]
                left += 1
            
            if l <= current_sum <= r:
                wins += 1
                current_sum = 0
                left = right + 1
                
        print(wins)



t = int(input())
for _ in range(t):
    solve()