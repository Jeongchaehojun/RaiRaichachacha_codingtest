#2025.08.30
#s2
#그래프 표현 문제
#BFS로써 큐
import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
connect = 0

for start in range(1, n + 1):
    if visited[start]:
        continue
    connect += 1
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for nx in graph[v]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
print(connect)