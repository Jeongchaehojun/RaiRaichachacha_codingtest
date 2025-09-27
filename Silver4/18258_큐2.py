#2025.09.27
#s4
import sys
from collections import deque


input = sys.stdin.readline
commands = input().splitlines()
queue = deque()

for command in commands:
    if command.startswith("push"):
        _, value = command.split()
        queue.append(value)
    elif command == "pop":
        print(queue.popleft() if queue else -1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        print(0 if queue else 1)
    elif command == "front":
        print(queue[0] if queue else -1)
    elif command == "back":
        print(queue[-1] if queue else -1)