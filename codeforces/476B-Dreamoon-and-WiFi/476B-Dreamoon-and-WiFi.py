from math import comb

s1 = input().strip()
s2 = input().strip()

target = s1.count('+') - s1.count('-')
current = s2.count('+') - s2.count('-')
q = s2.count('?')

diff = target - current

# Solve 2p - q = diff → p = (diff + q) / 2
if (diff + q) % 2 != 0:
    print(0.0)
else:
    p = (diff + q) // 2
    if p < 0 or p > q:
        print(0.0)
    else:
        favorable = comb(q, p)
        total = 2 ** q
        print(favorable / total)