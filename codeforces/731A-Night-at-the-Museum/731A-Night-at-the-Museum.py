import string

exhibit = input()
lowercase = string.ascii_lowercase
result = 0
currentPosition = 0

for char in exhibit:
    targetPosition = lowercase.index(char)
    distance = abs(targetPosition - currentPosition)
    result += min(distance, 26 - distance)  
    currentPosition = targetPosition

print(result)