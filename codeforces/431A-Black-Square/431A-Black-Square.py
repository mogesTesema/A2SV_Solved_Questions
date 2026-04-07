strips = list(map(int,input().split()))
process = input()
process = list(int(x) for x in process)
energy =0
for  i in process:
    energy += strips[i-1]
print(energy)