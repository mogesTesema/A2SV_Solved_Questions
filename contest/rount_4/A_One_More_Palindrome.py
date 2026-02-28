from collections import Counter
def solve():
    s = input()
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] == s[right] and left + 1 != right -1 and s[left + 1] == s[right-1] and s[left] != s[left + 1]:
            print("YES")
            return
        left += 1
        right -= 1
    print("NO")

t = int(input())
for _ in range(t):
    solve()