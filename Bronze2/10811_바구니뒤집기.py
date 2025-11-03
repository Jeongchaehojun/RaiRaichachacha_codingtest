#2025.11.3
#b2
N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]  # 뒤집기

print(*basket)
