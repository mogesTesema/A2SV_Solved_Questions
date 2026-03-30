n = int(input())
s = input()

total_L = s.count('L')
total_O = s.count('O')

left_L = 0
left_O = 0

for k in range(1, n):  # split after k elements
    if s[k-1] == 'L':
        left_L += 1
    else:
        left_O += 1

    right_L = total_L - left_L
    right_O = total_O - left_O

    if left_L != right_L and left_O != right_O:
        print(k)
        break
else:
    print(-1)