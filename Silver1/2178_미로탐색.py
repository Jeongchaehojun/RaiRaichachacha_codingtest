#2025.09.12
#s1
#
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
miro =[list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
            x, y = queue.popleft()
            
            # 현재 위치에서 4방향 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 범위를 벗어나면 무시
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                # 벽이면 무시
                if miro[nx][ny] == 0:
                    continue
                # 처음 방문하는 길이면 거리 갱신
                if miro[nx][ny] == 1:
                    miro[nx][ny] = miro[x][y] + 1
                    queue.append((nx, ny))
    return miro[N-1][M-1]
print(bfs(0,0))