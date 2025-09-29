#2025.09.29
#s1
import sys
import heapq


input = sys.stdin.readline
n = int(input().strip())
heap = []

for _ in range(n):
    x = int(input().strip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))