#2025.05.16
#b4
import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    sys.stdout.write(str(A+B) + '\n')

    #표준입력