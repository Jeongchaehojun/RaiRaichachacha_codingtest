#2025.06.22
#b3
import sys
input = sys.stdin.readline

for _ in range(3):  # 테스트셋은 3개
    n = int(input())
    total = 0
    for _ in range(n):
        total += int(input())

    if total > 0:
        print('+')
    elif total < 0:
        print('-')
    else:
        print('0')
