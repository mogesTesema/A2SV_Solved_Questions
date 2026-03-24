# def solve():
#     n = int(input())
#     letter = list(input())

#     stack = []


#     i = 0

#     while i < len(letter):
#         if (i+1) % 2 == 0:
#             stack.append(letter[i])
#             i += 1
#         else:
#             curr = i+1
#             stack.append(letter[i])

#             while curr < len(letter) and letter[i] == letter[curr]:
#                 curr += 1
           
#             if curr == i:
#                 i += 1
#             else:
#                 i = curr



#     if len(stack) % 2 == 0:
#         print(len(letter)-len(stack))
#         print("".join(stack))
#     else:
#         if stack:
#             stack.pop()
#             print(len(letter)-len(stack))
#             print("".join(stack))
#         else:
#             print(0)
            

# solve()


n = int(input())
s=input()

arr = []

for char in s:
    if len(arr) % 2 == 1:
        if arr[-1] == char:
            arr.pop()
        arr.append(char)
    else:
        arr.append(char)

if len(arr) % 2 == 1:
    arr.pop()

print(n-len(arr))
print("".join(arr))