#2025.11.05
#b3
max_value = -1
max_row = 0
max_col = 0

for i in range(1, 10):              # 행 번호
    row = list(map(int, input().split()))
    for j, val in enumerate(row, start=1):  # 열 번호
        if val > max_value:
            max_value = val
            max_row = i
            max_col = j

print(max_value)
print(max_row, max_col)
