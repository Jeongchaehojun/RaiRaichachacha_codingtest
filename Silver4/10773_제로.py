#2025.06.12
#s4
import sys

input = sys.stdin.readline
K = int(input())
stack = []

for _ in range(K):
    num = int(input())
    if num == 0:
        if stack: #비어있지 않으면 True, 비었으면 False
            stack.pop()
    else:
        stack.append(num)
print(sum(stack))
