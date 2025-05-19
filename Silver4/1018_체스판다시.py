#2025.05.18
#s4
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())
min_count = 64

for start_row in range(N - 7):
    for start_col in range(M - 7):
        # 패턴1: 왼쪽 위가 W로 시작하는 체스판
        count1 = 0
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    expected = 'W'
                else:
                    expected = 'B'
                if board[start_row + i][start_col + j] != expected:
                    count1 += 1
        
        # 패턴2: 왼쪽 위가 B로 시작하는 체스판
        count2 = 0
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    expected = 'B'
                else:
                    expected = 'W'
                if board[start_row + i][start_col + j] != expected:
                    count2 += 1
        min_count = min(min_count, count1, count2)

print(min_count)

