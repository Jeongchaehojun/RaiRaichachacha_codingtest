#2025.07.27
#s
#그리디 알고리즘 판다
import sys #이걸 해야함 그래야 둘째줄부터 쭉 받음
N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline())) #이거 하면 끝

coins.reverse() #내림차순

cnt = 0

for coin in coins:
    if K == 0:
        break
    cnt += K // coin
    K %= coin #이거 두 줄이 그냥 국룰임
print(cnt)