#2025.05.31
#s5

import sys
input = sys.stdin.readline
N = int(input())
points = []

for _ in range(N):
    x,y = map(int, input().split())
    points.append((x,y))
points.sort() #튜플 첫 요소 기준 정렬

for x, y in points:
    print(x,y)
