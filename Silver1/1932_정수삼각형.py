#2025.09.23
#s1
import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)] #dp테이블



for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0: #제일 왼쪽 원소
            triangle[i][j] += triangle[i - 1][j]
        elif j == len(triangle[i]) - 1: #제일 오른쪽 원소
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

print(max(triangle[-1])) #마지막 줄에서 최댓값

'''아래는 dp테이블 따로 만들어서 푼거'''

# dp = [[0] * (i + 1) for i in range(n)]

# # 초기값 (맨 위)
# dp[0][0] = triangle[0][0]

# # 점화식 적용
# for i in range(1, n):
#     for j in range(i + 1):
#         if j == 0:  # 왼쪽 끝
#             dp[i][j] = dp[i-1][j] + triangle[i][j]
#         elif j == i:  # 오른쪽 끝
#             dp[i][j] = dp[i-1][j-1] + triangle[i][j]
#         else:  # 중간
#             dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

# # 마지막 줄에서 최댓값 출력
# print(max(dp[n-1]))
