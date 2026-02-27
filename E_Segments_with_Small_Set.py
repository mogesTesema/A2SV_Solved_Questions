n, k = map(int, input().split())
nums = list(map(int, input().split()))

from collections import defaultdict

left = 0
freq = defaultdict(int)
unique = 0
ans = 0

for right in range(n):
    if freq[nums[right]] == 0:
        unique += 1
    freq[nums[right]] += 1

    while unique > k:
        freq[nums[left]] -= 1
        if freq[nums[left]] == 0:
            unique -= 1
        left += 1

    ans += right - left + 1

print(ans)