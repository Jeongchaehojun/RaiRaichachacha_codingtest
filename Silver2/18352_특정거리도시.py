#2025.06.16
#s2
#다익스트라 알고리즘. 오늘 자료구조 시험임..;
#근데 이거 bfs로 푸는게 적절..
import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)] #인접 리스트

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 거리 배열 (-1로 초기화, 방문하지 않은 노드 의미)
distance = [-1] * (n + 1)
distance[x] = 0  # 출발 도시 거리는 0

# BFS
queue = deque([x])

while queue:
    now = queue.popleft()
    for next_city in graph[now]:
        if distance[next_city] == -1:
            distance[next_city] = distance[now] + 1
            queue.append(next_city)

# 결과 출력
result = []
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)

if result:
    result.sort()
    for city in result:
        print(city)
else:
    print(-1)
