#2025.09.18
#s1
#dp
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2]) #R
    cost[i][1] += min(cost[i-1][0], cost[i-1][2]) #G
    cost[i][2] += min(cost[i-1][0], cost[i-1][1]) #B
    #왜 이렇게 되는거임?

print(min(cost[-1]))