def solve():
    n,k = map(int, input().split())
    layers = list(set(input()))

    letter = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    # b, e, l, m, o, p, r
    layers.sort()
    if len(layers) < k:
        print(-1)
        return
    if k > 13:
        print(-1)
        return
    stack = []
    w = 0

    for layer in layers:
        if not stack:
            stack.append(layer)
            w += letter[layer]
        else:
            elem = stack[-1]
            if letter[elem] +1 < letter[layer] and len(stack) < k:
                stack.append(layer)
                w += letter[layer]
    if len(stack) != k:
        print(-1)
        return
    print(w)


solve()