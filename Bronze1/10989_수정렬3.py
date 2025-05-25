#2025.05.25
#b1
""" T = int(input())
lst = []
for _ in range(T):
    lst.append(int(input().strip()))
lst.sort()
for i in lst:
    print(i) """
#메모리 초과가 발생함
import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001
for _ in range(N):
    num = int(input())
    count[num] += 1
for i in range(1, 10001):
    for _ in range(count[i]):
        print(i)