# Build tree
for i in range(2, n + 1):
    p = int(input())
    children[p].append(i)

# Check spruce condition
for v in range(1, n + 1):
    if len(children[v]) > 0:  # non-leaf
        leaf_count = 0
        for u in children[v]:
            if len(children[u]) == 0:
                leaf_count += 1
        if leaf_count < 3:
            print("No")
            exit()

print("Yes")