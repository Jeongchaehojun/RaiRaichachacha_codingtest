#2025.06.19
#b4
X = int(input())
N = int(input())

total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += a*b
print("Yes" if total == X else "No")