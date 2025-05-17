#2025.05.17
#b3
temp = 0
count = 0
for i in range(9):
    n = int(input())
    if n > temp:
        temp = n
        count = i+1
print(temp)
print(count)