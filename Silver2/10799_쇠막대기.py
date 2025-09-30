#2025.09.30
#s2
import sys
input = sys.stdin.readline

data = input().strip()
stack = []
result = 0

for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if data[i - 1] == '(':
            result += len(stack)
        else:
            result += 1

print(result)