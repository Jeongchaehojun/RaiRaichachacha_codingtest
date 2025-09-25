#2025.09.25
#s2
import sys
import heapq

input = sys.stdin.readline
n = int(input().strip())
min_heap = [] #최소힙

for _ in range(n):
    x = int(input().strip()) #얘도 있어야함
    if x == 0:
        print(heapq.heappop(min_heap) if min_heap else 0)
    else:
        heapq.heappush(min_heap, x)
