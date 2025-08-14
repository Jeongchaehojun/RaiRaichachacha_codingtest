#2025.08.14
#g5
#dp문제임
#0-1knapsack 문제를 그리디로 풀 수 없다는 것을 수업시간에 배웠었음
#factional knapsack이면 다르겠지만 이건 가능한 모든 것을 다 해봐야하니 DP

N, K = map(int, input().split())
item = []

for _ in range(N):
    item.append(list(map(int, input().split())))

#dp[w] = w에서 얻을 수 있는 최대 가치
dp = [0] * (K+1) #+1해주는거!!!!

for weight, value in item:
    for w in range(K, weight -1, -1): #거꾸로
        dp[w] = max(dp[w], value + dp[w - weight])

print(dp[K])