def solve():
    n = int(input())
    s = input()
    typed = ""

    for i in range(len(s)):
        if s[i] in typed:
            if i+1 < len(s):
                if s[i] +s[i+1] in typed:
                    print("YES")
                    return
                typed += s[i]
            else:
                typed += s[i]
            
        else:
            typed += s[i]
    print("NO")

t = int(input())
for _ in range(t):
    solve()