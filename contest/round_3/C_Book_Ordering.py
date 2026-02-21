def solve():
    n = int(input())
    
    books = []
    for _ in range(n):
        w, h = map(int, input().split())
        books.append((w, h))

    prev_max = 10**18  

    for w, h in books:
        big = max(w, h)
        small = min(w, h)

        if big <= prev_max:
            prev_max = big
        elif small <= prev_max:
            prev_max = small
        else:
            print("NO")
            return

    print("YES")


solve()