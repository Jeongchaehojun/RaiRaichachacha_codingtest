#2025.08.17
#g3
#dp문제입니다. 약간 운영체제스러움
N, M = map(int, input().split())
memories = list(map(int, input().split())) #메모리
cs = list(map(int, input().split())) #비용

total_c = sum(c) #모든 앱 비용 합
dp = [0] * (total_c + 1)

for i in range(N):
    m, c = memories[i], cs[i]
    for j in range(total_c, c-1, -1):
        dp[j] = max(dp[j], dp[j-c]+m)

for j in range(total_c + 1):
    if dp[j] >= M:
        print(j)
        break