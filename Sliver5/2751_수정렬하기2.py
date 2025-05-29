#2025.05.30
#s5
""" N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input().strip()))
sorted_lst = sorted(lst)
for num in sorted_lst:
    print(num) """
#실버문제 치고는 easy인 줄 알았으나 시간 초과임
#N이 개큼

import sys

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
lst.sort()
result = '\n'.join(map(str, lst))
sys.stdout.write(result + '\n')