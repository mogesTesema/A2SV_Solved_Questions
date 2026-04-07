n = int(input())
teams = []
for i in range(n):
    teams.append(list(map(int, input().split(" "))))
hostCounter = 0
for i in range(n):
    for j in range(i+1,n):
        if teams[i][0] == teams[j][1]:
            hostCounter +=1
        if teams[i][1] == teams[j][0]:
            hostCounter += 1
print(hostCounter)