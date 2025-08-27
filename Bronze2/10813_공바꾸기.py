#2025.08.27
#b2
N, M = map(int, input().split())
baguni = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, input().split())
    baguni[i-1], baguni[j-1] = baguni[j-1], baguni[i-1]
print(*baguni)