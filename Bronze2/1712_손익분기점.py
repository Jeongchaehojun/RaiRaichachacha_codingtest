#2025.10.17
#b2
A, B, C = map(int, input().strip().split())
if C <= B:
    print(-1)
else:
    print(A // (C - B) + 1)