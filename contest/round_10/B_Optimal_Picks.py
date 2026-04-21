def solve():
    n, k = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort(reverse=True)

    ev = 0
    nv = 0
    et = True
    # print("unmodified",nums)
    for i in range(len(nums)):
        if et:
            et = False
        else:
            if k > 0 and nums[i] < nums[i-1]:
                curr_diff = nums[i-1] - nums[i]
                if k >= curr_diff:
                    nums[i] += curr_diff
                    k -= curr_diff
                else:
                    nums[i] += k
                    k = 0
                    break

            
            et = True
    # print("modified",nums)
    et = True
    for i in range(len(nums)):
        if et:
            ev += nums[i]
            et = False
        else:
            nv += nums[i]
            et = True

    diff = ev - nv
    # print("ev - nv",ev,nv)
    print(diff)

t = int(input())

for _ in range(t):
    solve()