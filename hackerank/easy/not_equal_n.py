if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x = list(range(0,x+1))
    y = list(range(0,y+1))
    z = list(range(0,z+1))
    ans = []
    for a in x:
        for b in y:
            for c in z:
                if a+b+c != n:
                    ans.append([a,b,c])
    print(ans)