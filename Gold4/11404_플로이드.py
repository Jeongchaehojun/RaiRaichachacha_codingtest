#2025.09.11
#g4
#플로이드-워셜
#사실상 외워서 푸는거임 i -> k+k -> j 거칠 때 짧으면 갱신
import sys
input = sys.stdin.readline
INF = 10**9 #인피니티

n = int(input())
m = int(input())

#지금 위치를 0으로 하고 나머지를 INF로 초기화
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

#버스 정보 입력 처리
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c) #최소 비용만 저장

#플로이드 워셜 3중 포문 시바럴
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()#줄바꿈
