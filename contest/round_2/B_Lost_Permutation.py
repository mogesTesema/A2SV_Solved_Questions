from collections import Counter
def solve():
    n,s = [int(x) for x in input().split()]

    nums = [int(x) for x in input().split()]
    min_val = min(nums)
    max_val = max(nums)
    
    # edge
    if min_val <=0:
        print("NO")
        return
    counted = Counter(nums)
    for val in counted.values():
        if val > 1:
            print("NO")
            return
        
    original = set(range(1,max_val+1))
    num_set = set(nums)
    lost = list(original-num_set)
    lost_sum = sum(lost)

    if lost_sum > s:
        print("NO")
        return
    remain = s - lost_sum
    next = max_val +1

    while remain > next and remain > 0:
        remain -= next
        next += 1

    if remain > 0 and next > remain:
        print("NO")
    elif remain < 0:
        print("NO")
    else:
        print("YES")

t = int(input())
for _ in range(t):
    solve()