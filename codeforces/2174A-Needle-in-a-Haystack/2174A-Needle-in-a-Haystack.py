def solve():
    T_str = input().strip()
    T = int(T_str)
    
    for _ in range(T):
        s = input().strip()
        t = input().strip()
        
        pool = [0] * 26
        for char in t:
            pool[ord(char) - 97] += 1
            
        req = [0] * 26
        for char in s:
            req[ord(char) - 97] += 1
            
        possible = True
        for i in range(26):
            if pool[i] < req[i]:
                possible = False
                break
        
        if not possible:
            print("Impossible")
            continue
            
        res = []
        res_append = res.append
        s_idx = 0
        n_s = len(s)
        n_t = len(t)
        
        s_ords = [ord(c) - 97 for c in s]
        
        for _ in range(n_t):
            for i in range(26):
                if pool[i] > 0:
                    if s_idx < n_s and i == s_ords[s_idx]:
                        pool[i] -= 1
                        req[i] -= 1
                        s_idx += 1
                        res_append(chr(97 + i))
                        break
                    elif pool[i] > req[i]:
                        pool[i] -= 1
                        res_append(chr(97 + i))
                        break
                            
        print("".join(res))

solve()