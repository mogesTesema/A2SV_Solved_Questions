def solve():
    n = int(input())
    nums = list(map(int,input().split()))
  
    ans = []
    def is_sort(a):
        return all(a[i] <= a[i+1] for i in range(len(a)-1))
    
    def change(path):
        m = max(path)
        all = list(range(m+1))
        all = set(all)
        diff = list(all - set(path))
        diff.sort()
        if len(diff) == 0:
            diff.append(m+1)
        index = diff[0]
        if index == 0:
            path[0] = 0
            ans.append(1)
        else:
            path[index-1] = index
            ans.append(index)


    
    for i in range(2*n):

        if is_sort(nums):
            print(i+1)
            print(" ".join([str(x) for x in ans]))
            return
        change(nums)








t = int(input())
for _ in range(t):
    solve()