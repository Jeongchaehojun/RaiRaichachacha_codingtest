#2025.08.04
#g4
#다익스트라 알고리즘입니다.
#우선 순위 큐를 기반으로 한 다익스트라 알고리즘
import sys
import heapq #이게 우선순위 큐 기반

input = sys.stdin.readline
INF = int(1e9) #1000000000 10억이랑 같은거래.. 
#아직 방문 안했거나 못가는 곳
V, E = map(int, input().split()) #vertex 정점, edge 간선
K = int(input()) #시작 v

graph = [[] for _ in range(V + 1)] #인접 리스트

#간선 정보
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w)) #u에서 v로 가는 가중치 w

#최단 거리 저장 리스트
distance = [INF] * (V + 1)
distance[K] = 0 #시작이라서 0

q = []
heapq.heappush(q, (0,K)) #큐에다가 (거리,정점)을 push

while q:
    dist, now = heapq.heappop(q) #팝 해가면서 검사

    if dist > distance[now]: #이미 짧으면 continue
        continue

    for next_node, weight in graph[now]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, (cost, next_node))

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])