from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = defaultdict(int)
left = 0
unique = 0
best_len = 0
best_l = 0
best_r = 0

for right in range(n):
    if freq[a[right]] == 0:
        unique += 1
    freq[a[right]] += 1

    while unique > k:
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            unique -= 1
        left += 1

    if right - left + 1 > best_len:
        best_len = right - left + 1
        best_l = left
        best_r = right

print(best_l + 1, best_r + 1)