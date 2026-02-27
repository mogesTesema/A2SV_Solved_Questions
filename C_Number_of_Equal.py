from collections import Counter
n,m = map(int,input().split())

first = list(map(int,input().split()))
second = list(map(int,input().split()))
union = set(first) & set(second)
fc = Counter(first)
sc = Counter(second)

ans = 0

for elem in union:
    ans += fc[elem]*sc[elem]

print(ans)
