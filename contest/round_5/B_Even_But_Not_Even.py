def solve():
    n = int(input())
    s = input().strip()

    a = [int(d) for d in s]

    last_odd_inx = -1
    for i in range(n-1,-1,-1):
        if a[i]%2 != 0:
            last_odd_inx = i
            break

    if last_odd_inx == -1:
        print("-1")
        return
    
    pref = [0]*(n+1)

    for i in range(n):
        pref[i+1] = pref[i] + a[i]

    current_sum = pref[last_odd_inx+1]
    if current_sum %2 == 0:
        print(s[:last_odd_inx+1])
    else:
        remove_idx = -1
        for i in range(last_odd_inx-1,-1-1):
            if a[i] %2 != 0:
                remove_idx = i
                break
        if remove_idx == -1:
            print("-1")
        else:
            res = s[:remove_idx] +s[remove_idx+1:last_odd_inx+1]
            print(res)

   

   


   

    


t = int(input())
for _ in range(t):
    solve()