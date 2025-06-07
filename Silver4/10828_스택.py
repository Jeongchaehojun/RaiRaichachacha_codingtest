#2025.06.07
#s4
import sys

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        print(stack.pop() if stack else -1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(0 if stack else 1)
    elif cmd[0] == "top":
        print(stack[-1] if stack else -1)

