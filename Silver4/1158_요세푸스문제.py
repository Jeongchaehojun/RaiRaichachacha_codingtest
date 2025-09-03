#2025.09.03
#s4
from collections import deque

N, K = map(int, input().split())
deq = deque(range(1, N+1))
result = []

while deq:
    deq.rotate(-(K-1))
    result.append(deq.popleft())
print("<" + ", ".join(map(str,result)) + ">")