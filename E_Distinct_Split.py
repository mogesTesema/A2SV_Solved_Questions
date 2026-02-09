from collections import Counter

def distinct():
    _ = int(input())
    chars = list(input().split())
    left = dict()
    right = Counter(chars)
    max_value =len(right)+len(left)
    right_elems = right.keys()

    for elem in chars:
        if elem in right:
            if right[elem] == 1:
                right_elems.pop(elem)
                right[elem] = 0
            else:
                right[elem] -= 1
        left[elem] = left.get(elem,0) + 1
        max_value = max(max_value,len(right)+len(left))
    print(max_value)

t = int(input())
for _ in range(t):
    distinct()
        
        





    
