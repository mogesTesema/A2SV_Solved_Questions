cardNo = int(input())
cards = list(map(int, input().split()))
sereja = 0
dima = 0
start = True
while(len(cards)):
    if start:
        if cards[0] > cards[-1]:
            sereja += cards[0]
            cards.pop(0)
        else:
            sereja += cards[-1]
            cards.pop()
        start = False
    else:
        if cards[0] > cards[-1]:
            dima += cards[0]
            cards.pop(0)
        else:
            dima += cards[-1]
            cards.pop()
        start = True
print(sereja, dima)