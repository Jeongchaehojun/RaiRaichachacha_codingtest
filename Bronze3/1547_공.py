#2025.06.25
#b3
M = int(input().strip())
pos = 1 #공 시작위치

for _ in range(M):
    X, Y = map(int, input().split())
    if pos == X:
        pos = Y
    elif pos == Y:
        pos = X

print(pos)
