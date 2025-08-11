#2025.08.11
#s3
#삼성전자 코테 문제인데 읽자마자 그리디임
#근데 그리디가 아니라 DP였다!!!
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 2)

for i in range(n, 0, -1):
    Ti, Pi = arr[i-1]
    if i + Ti <= n + 1:
        dp[i] = max(Pi + dp[i + Ti], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[1])


