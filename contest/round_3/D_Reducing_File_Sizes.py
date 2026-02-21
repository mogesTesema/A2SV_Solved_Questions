n,m = list(int(x) for x in input().split())
files = []

for _ in range(n):
    file = list(int(x) for x in input().split())
    diff = file[0] - file[1]
    file.append(diff)
    files.append(file[::-1])

files.sort(reverse=True)
# print(files)
b_sum = 0
for file in files:
    b_sum += file[2]
i= 0
while b_sum > m and i < len(files):
    b_sum -= files[i][0]
    i += 1

if i == len(files) and b_sum > m:
    print(-1)
else:
    print(i)