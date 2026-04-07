def palindrome():
    n = int(input())
    vowls = "aeiou"
    if n<=5:
        print(vowls[:n])
        return
    answer = list(vowls)
    while(len(answer)< n):
        lowest = answer[0]
        for i in range(len(answer)):
            if answer.count(lowest) > answer.count(answer[i]):
                lowest = answer[i]
        answer.insert(answer.index(lowest),lowest)
    answer = "".join(answer)
    print(answer)



test = int(input())
for _ in range(test):
    palindrome()