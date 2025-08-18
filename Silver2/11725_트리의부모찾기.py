#2025.08.18
#s2
#트리 관련 문제
#dfs로 찾는 문제임
import sys
sys.setrecursionlimit(10**6) #이거 없으면 recursion 에러가 뜸;;;
input = sys.stdin.readline

#dfs 방식
def dfs(v):
    for next in graph[v]:
        if parents[next] == 0:  # 아직 방문하지 않은 경우
            parents[next] = v
            dfs(next)

N = int(input())

graph = [[] for _ in range(N + 1)]

parents = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2, N + 1):
    print(parents[i])
