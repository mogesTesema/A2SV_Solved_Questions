def solve():
    n = int(input())

    counter = 1
    # a = 0
    # b = 0
    aw = 0
    ab = 0
    bw = 0
    bb = 0
    is_white = True
    a_turn = False
    if n > 0:
        # a = 1
        n -= 1
        counter +=1
        aw += 1
        is_white = False
    else:
        print(0,0)


    while n > 0:

        if a_turn:
            for i in range(2):
                if n >= counter:
                    # a += counter
                    n -= counter
                    q = counter//2
                    r = counter %2
                    if r == 0:
                        aw += q
                        ab += q
                    else:
                        if is_white:
                            aw += q + 1
                            ab += q
                            is_white = False
                        else:
                            ab += q +1
                            aw += q
                            is_white = True

                else:
                    # a += n
                    q = n//2
                    r = n %2
                    n = 0

                    if  r == 0:
                        aw += q 
                        ab += q

                    elif is_white:
                            aw += q + 1
                            ab += q
                            is_white = False
                    else:
                        ab += q +1
                        aw += q
                        is_white = True

                counter += 1

            a_turn = False
        else:
            for i in range(2):
                if n >= counter:
                    # b += counter
                    n -= counter
                    q = counter//2
                    r = counter %2
                    if r == 0:
                        bw += q
                        bb += q
                    else:
                        if is_white:
                            bw += q + 1
                            bb += q
                            is_white = False
                        else:
                            bb += q +1
                            bw += q
                            is_white = True

                else:
                    # b += n
                    q = n//2
                    r = n %2
                    n = 0
                    if r == 0:
                        bw += q
                        bb += q

                    elif is_white:
                            bw += q + 1
                            bb += q
                            is_white = False
                    else:
                        bb += q +1
                        bw += q
                        is_white = True

                counter += 1

            a_turn = True
    print(aw,ab,bw,bb)



t = int(input())

for _ in range(t):
    solve()