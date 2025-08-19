#2025.08.19
#s4
#구현 문제
#Deque
import sys
from collections import deque
#여기까지 그냥 암기..

input = sys.stdin.readline

N = int(input())
dq = deque()

for _ in range(N):
    T = input().split()
    op = T[0] #operation 연산이라는 뜻이여

    if op == 'push_front':
        dq.appendleft(int(T[1]))
    elif op == 'push_back':
        dq.append(int(T[1]))
    elif op == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif op == 'pop_back':
        print(dq.pop() if dq else -1)
    
    elif op == 'size':
        print(len(dq))
    elif op == 'empty':
        print(0 if dq else 1)
    elif op == 'front':
        print(dq[0] if dq else -1)
    elif op == 'back':
        print(dq[-1] if dq else -1)