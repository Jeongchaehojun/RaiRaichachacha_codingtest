#2025.05.16
#b3
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    result = [A[i][j] + B[i][j] for j in range(M)]
    print(*result) #공백을 구분해서 출력
