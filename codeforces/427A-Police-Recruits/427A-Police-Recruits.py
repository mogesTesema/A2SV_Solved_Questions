occurance = int(input())
crimePolice = list(map(int, input().split()))
untreated = 0
police = 0
for i in range(occurance):
    if crimePolice[i] != -1:
        police += crimePolice[i]
    else:
        if police == 0:
            untreated += 1
        else:
            police -= 1
print(untreated)