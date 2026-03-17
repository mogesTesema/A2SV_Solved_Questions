def solve():
    def get_tokens():
        while True:
            try:
                line = input().split()
                if not line:
                    continue
                yield from line
            except EOFError:
                break
    
    tokens = get_tokens()
    t_str = next(tokens, None)
    if t_str is None:
        return
    
    t = int(t_str)
    for _ in range(t):
        n = int(next(tokens))
        s = [int(next(tokens)) for _ in range(n)]
        
        ans = [0] * n
        possible = True
        i = 0
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i += 1
            
            group_size = i - start
            if group_size < 2:
                possible = False
                break
            
            for k in range(start, i - 1):
                ans[k] = k + 2
            ans[i - 1] = start + 1
            
        if not possible:
            print("-1")
        else:
            print(*(ans))

if __name__ == "__main__":
    solve()