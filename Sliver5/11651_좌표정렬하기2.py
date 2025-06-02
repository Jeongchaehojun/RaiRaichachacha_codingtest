#2025.06.02
#s5
#아래는 좌표 정렬하기 1 코드.
"""
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

"""
import sys
input = sys.stdin.readline
N = int(input())
points = []

for _ in range(N):
    x,y = map(int, input().split())
    points.append((x,y))
points.sort(key=lambda p: (p[1], p[0])) #lambda 부분만 다른 것

for x, y in points:
    print(x,y)
