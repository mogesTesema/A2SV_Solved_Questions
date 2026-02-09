def solve():
    digits = input()
    if len(digits) == 0:
        print(-1)
        return
    first = digits[0]
    second = ""
    for index, digit in enumerate(digits[1:]):
        if digit == "0":
            first += digit
        else:
            second = digits[index+1:]
            break
    if len(first) == 0 or len(second) == 0:
        print(-1)
        return
    first = int(first)
    second = int(second)
    if first <= 0 or second <= 0:
        print(-1)
    elif first >= second:
        print(-1)
    else:
        print(first,second)

t = int(input())
for _ in range(t):
    solve()

