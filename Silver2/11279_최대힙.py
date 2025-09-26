#2025.09.26
#s2
import sys
import heapq


input = sys.stdin.readline
n = int(input().strip())
heap = []

for _ in range(n):
    x = int(input().strip())
    if x == 0:
        if heap: #여기서 이중 조건
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)