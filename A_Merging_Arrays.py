n, m = list(int(x) for x in input().split())
first = list(int(x) for x in input().split())
second = list(int(x) for x in input().split())

fp = 0
sp = 0
new_arr = []

while fp < len(first) and sp < len(second):
    if first[fp] < second[sp]:
        new_arr.append(first[fp])
        fp += 1
    else:
        new_arr.append(second[sp])
        sp += 1

new_arr.extend(first[fp:])
new_arr.extend(second[sp:])
ans = " ".join([str(x) for x in new_arr])
print(ans)