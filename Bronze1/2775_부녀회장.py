#2025.05.23
#b1

T = int(input())

# 15x15 배열 (1부터 시작이므로 0~14까지)
dp = [[0] * 15 for _ in range(15)]

# 0층 초기화
for i in range(1, 15):
    dp[0][i] = i

# 나머지 층 채우기
for k in range(1, 15):
    for n in range(1, 15):
        dp[k][n] = dp[k][n-1] + dp[k-1][n]

# 테스트 케이스 입력 처리
for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])
