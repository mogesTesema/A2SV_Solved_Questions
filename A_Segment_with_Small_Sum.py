n,s = list(int(x) for x in input().split())
nums = list(int(x) for x in input().split())

curr_sum = 0
left = 0
max_len = 0

for i in range(n):

    curr_sum += nums[i]
    while curr_sum > s:
        curr_sum -= nums[left]
        left += 1

    max_len = max(max_len,i-left +1)
print(max_len)
    