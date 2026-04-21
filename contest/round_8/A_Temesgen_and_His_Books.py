def solve():
    n = int(input())
    books = list(map(int, input().split()))
    books.sort()
    print(books[-1] + books[-2])
    

t = int(input())
for _ in range(t):
    solve()
    