stone = input()
instruction = input()
counter =0
for i in instruction:
    if i == stone[counter]:
        counter +=1
print(counter+1)