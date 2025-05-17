#2025.05.17
#b2
T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    result = ' '
    for char in S:
        result += char * R
    print(result)