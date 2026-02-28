def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    ans = 0

    left = 0
    while left < len(nums)-1:
        ans += min(nums[left],nums[left+1])
        left += 2

    print(ans)

t = int(input())
for _ in range(t):
    solve()