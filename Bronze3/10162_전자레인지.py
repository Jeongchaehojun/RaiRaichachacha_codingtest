#2025.10.04
#b3
import sys
input = sys.stdin.readline

time = int(input())
buttons = [300, 60, 10]
result = []

for button in buttons:
    result.append(time // button)
    time %= button

if time != 0:
    print(-1)
else:
    print(*result)