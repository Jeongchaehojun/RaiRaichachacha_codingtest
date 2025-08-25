#2025.08.25
#s3
#그래프 이론에서 문제를 찾음. 
#dfs로 접근
###근데 dfs를 쓸 때면 재귀 깊이를 sys.setrecursionlimit(10**6) 이런걸 해줘야 함 
#시간복잡도 O(n+m)
import sys
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(now):
    visited[now] = True
    cnt = 0
    for next in graph[now]:
        if not visited[next]:
            cnt += 1
            cnt += dfs(next)
    return cnt #이거 들여쓰기 위치 때매 틀림...
    
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = dfs(1)
print(result)
    