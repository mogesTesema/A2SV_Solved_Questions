def solve():
    n = int(input())
    year = input()

    last_year = "2025"
    this_year = "2026"

    if last_year not in year or this_year in year:
        print(0)
    else:
        print(1)

t = int(input())
for _ in range(t):
    solve()