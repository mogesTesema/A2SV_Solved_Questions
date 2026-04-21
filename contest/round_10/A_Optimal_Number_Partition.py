n = int(input())
nums = list(map(int,input().split()))
nums.sort()
total = 0
nums.sort()
left = 0 
right = len(nums) - 1

while left < right:
    total += (nums[left] + nums[right])**2
    left += 1
    right -= 1

print(total)