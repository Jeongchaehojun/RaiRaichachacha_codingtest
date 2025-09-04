#2025.09.04
#s3
#DP
#진짜 뒤!지게 햇갈린다..
import sys
input = sys.stdin.readline

N = int(input()) #계단 개수
score = [int(input()) for _ in range((N))] #각 계단 점수

if N == 1:
    print(score[0])
elif N == 2:
    print(score[0] + score[1])
else:
    dp = [0] * N
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])

    for i in range(3, N):
        dp[i] = max(
            dp[i - 2] + score[i], #뒤에서 두칸 전에 뛰어 넘는거
            dp[i - 3] + score[i - 1] + score[i] #뒤에서 3칸 전에서 뛰어서 1칸 전까지 갔다가 도착하는거
        )
    print(dp[N - 1])