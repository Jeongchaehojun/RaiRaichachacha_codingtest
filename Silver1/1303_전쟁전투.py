#2025.07.24
#s1
#병사의 상하좌우에 연결이 되어 있긴 한지 확인하는거 <- dfs

import sys
sys.setrecursionlimit(10000) #재귀 깊이 제한을 늘려야 한다고 알려줌

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(m)] #격자 만들기
visited = [[False] * n for _ in range(m)]

dx = [0, 0, -1, 1] #상하좌우 (한 칸 왼쪽으로도 보고 한 칸 오른쪽으로도 봄
dy = [-1, 1, 0, 0]

def dfs(x, y, team):
    visited[x][y] = True #현재위치는 방문해서 true
    count = 1 #자기 자신 한 명이라서 1로 시작
    for i in range(4): #상하좌우 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n: #m, n범위 안이고, 
            if not visited[nx][ny] and grid[nx][ny] == team: #방문 안했고, 같은 팀이면
                count += dfs(nx, ny, team) #카운트 더하는게 재귀적으로 
    return count

white = 0
blue = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            power = dfs(i, j, grid[i][j])
            if grid[i][j] == 'W':
                white += power **2
            else:
                blue += power **2
print(white, blue)