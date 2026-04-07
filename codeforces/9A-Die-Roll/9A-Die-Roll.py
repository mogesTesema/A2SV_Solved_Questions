import math
y, w = list(map(int, input().split()))
minPoint = max(y,w)
if minPoint ==0:
    totalPoints = 6
else:
    totalPoints = 6 -minPoint +1

divisor = math.gcd(totalPoints,6)
print(f"{int(totalPoints/divisor)}/{int(6/divisor)}")