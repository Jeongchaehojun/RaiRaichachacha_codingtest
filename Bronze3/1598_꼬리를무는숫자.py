#2025.06.26
#b3
a, b = map(int, input().split())

# 좌표 구하기
a_row, a_col = (a - 1) // 4, (a - 1) % 4
b_row, b_col = (b - 1) // 4, (b - 1) % 4

# 맨해튼 거리 출력
print(abs(a_row - b_row) + abs(a_col - b_col))
