#2025.10.10
#b2
import sys
input = sys.stdin.readline

n = int(input().strip())

if n == 0:
    print(0)
    sys.exit(0)

dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])