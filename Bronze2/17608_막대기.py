#2025.09.05
#b2
import sys
input = sys.stdin.readline

n = int(input())
stick = [int(input()) for _ in range(n)]

cnt = 0
max_height = 0

for h in reversed(stick):
    if h > max_height:
        cnt += 1
        max_height = h

print(cnt)