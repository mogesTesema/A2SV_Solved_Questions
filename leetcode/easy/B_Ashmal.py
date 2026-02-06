def solve_ashmal():
    t = int(input())
    n = int(input())
    words = input().split()
    s = ""
    for word in words:
        if word < s:
            s = word + s
        else:
            s = s + word
    print(s)


solve_ashmal()