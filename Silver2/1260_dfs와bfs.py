#2025.08.06
#s2
import sys
from collections import deque #dfs, bfs쓸거면 deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

#인접 리스트 그래프 생성: 정점 번호가 1부터라서 0은 아니고
graph = [[] for _ in range(N+1)]

#간선 정보 받기
for _ in range(M):
    a, b = map(int, input().split()) #입력 들어오는 두 정점
    graph[a].append(b) #인접했다는거 인접 리스트에 추가 해주기
    graph[b].append(a) #무방향이라서 반대도 추가해주기

#인접리스트 오름차순 정렬
#정점번호가 작은 것부터라는 조건
for neigh in graph:
    neigh.sort()

visited = [False] * (N+1) #False로 일단 초기화
visited_bfs = [False] * (N+1)
result_dfs = []
result_bfs = []

#아래 있는 변수들은 전역변수라서 def 함수 선언을 맨 위에 갈겨도 되긴함

#방문한 곳을 True로 하고, 방문 '순서'를 리스트에 넣고, 안간 v가 있으면 가줌
def dfs(v):
    visited[v] = True
    result_dfs.append(v)
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)

#탐색 시작 정점 번호 받고, 큐 자료구조로 시작, 시작점 True
def bfs(start):
    q = deque([start])
    visited_bfs[start] = True
    while q: #q가 비어있지 않은 동안 반복
        v = q.popleft() #맨앞에서 꺼내기 O(1)
        result_bfs.append(v) #방문 했다고 '순서' 리스트에 넣어줌
        for nv in graph[v]: #그래프 안에 새로운 정점에 대해서
            if not visited_bfs[nv]: #안간 곳이 있다면 가야함
                visited_bfs[nv] = True #방문리스트에 넣어줌
                q.append(nv) #중복 삽입도 방지하고 인접정점을 큐 뒤에 넣기



dfs(V)
bfs(V)

print(*result_dfs) #쉼표로 구분되어 있는 리스트 요소를 공백으로 출력하게 하려고
print(*result_bfs) 