#2025.09.22
#s1
#dfs
#솔직히 이거 쌩으로 푸는건데 너무 오래걸려서 구글링함

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 집이 아니면 0 리턴
    if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] == 0:
        return 0
    graph[x][y] = 0  # 방문 처리 (집 없다고 바꿔버림)
    cnt = 1
    for i in range(4):
        cnt += dfs(x + dx[i], y + dy[i])
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:   # 아직 방문 안 한 집 발견
            result.append(dfs(i, j))

print(len(result))           # 단지 개수
for r in sorted(result):     # 단지 크기 오름차순
    print(r)