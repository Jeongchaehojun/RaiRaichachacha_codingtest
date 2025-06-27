#2025.06.27
#b2
N = int(input())
trophy = [int(input()) for _ in range(N)]

# 왼쪽
cnt_left = 0
mx = 0
for h in trophy:
    if h > mx:
        cnt_left += 1
        mx = h

# 오른쪽
cnt_right = 0
mx = 0
for h in reversed(trophy):
    if h > mx:
        cnt_right += 1
        mx = h

print(cnt_left)
print(cnt_right)

