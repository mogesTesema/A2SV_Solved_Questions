shoes = set(map(int, input().split(" ")))
if len(shoes) >= 4:
    print(0)
else:
    print( 4-len(shoes))