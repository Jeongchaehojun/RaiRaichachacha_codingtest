#2025.09.08
#g5
#dp
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

INF = 10 ** 9 #이거 인피니티임.. "아직 못 만든 수"
dp = [INF] * (k+1) #금액 i를 만드는 데 필요한 최소 동전 개수
dp[0] = 0 #0원은 따로 표현

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

print(dp[k] if dp[k] != INF else -1)