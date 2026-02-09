def solve():
    n = int(input())

    rates = list(input().split())
    student = []
    for index, value in enumerate(rates):
        student.append([value,index])
    student.sort(reverse=True)
    if len(rates) == 0 or n==0:
        return 
    current_score = student[0][0]
    position = 1

    for i in range(len(student)):
        if student[i][0] == current_score:
            rates[student[i][1]] = position
        else:
            current_score = student[i][0]
            position = i + 1
            rates[student[i][1]] = position

    ans = " ".join([str(x) for x in rates])
    print(ans)

solve()