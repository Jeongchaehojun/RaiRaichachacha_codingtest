import sys

#2025.09.24
#s3
input = sys.stdin.readline

def padovan(n):
    dp = [0] * (n + 1)
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 1
    if n >= 3:
        dp[3] = 1
    for i in range(4, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    return dp[n]

t = int(input())
cases = [int(input()) for _ in range(t)]

for case in cases:
    print(padovan(case))