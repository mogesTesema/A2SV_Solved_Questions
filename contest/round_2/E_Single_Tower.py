n = int(input())
towers = []
all_blocks = []

for _ in range(n):
    data = list(map(int, input().split()))
    k = data[0]
    blocks = data[1:]
    towers.append(blocks)
    all_blocks.extend(blocks)

sorted_blocks = sorted(all_blocks)
pos = {v: i for i, v in enumerate(sorted_blocks)}

good_segments = 0

for blocks in towers:
    i = 0
    while i < len(blocks):
        j = i
        while j + 1 < len(blocks) and pos[blocks[j + 1]] == pos[blocks[j]] + 1:
            j += 1
        good_segments += 1
        i = j + 1

splits = good_segments - n
combines = good_segments - 1

print(splits, combines)