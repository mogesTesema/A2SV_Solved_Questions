n  = int(input())
levels = [int(x) for x in input().split()]
all_level = set(range(1,n+1))
level_set = set(levels)
not_played = all_level - level_set
not_played = list(not_played)
print(not_played[0])