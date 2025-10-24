#2025.10.24
#g5
import sys
import math
input = sys.stdin.readline

#동작 횟수 최솟값을 구해야 함.
T = int(input().strip())

for _ in range(T):
    x, y = map(int, input().split())
    d = y - x

    # i*i < d ≤ i*(i+1)  이동횟수 = 2*i
    # i*(i+1) < d ≤ (i+1)*(i+1) 이동횟수 = 2*i + 1
    i = int(math.sqrt(d))

    if i * i == d:
        print(2 * i - 1)
    elif d <= i * (i + 1):
        print(2 * i)
    else:
        print(2 * i + 1)
# 1+2+3+4+3+2+1 = 16 = 4^2 이걸 아는 사람이 있냐 ㅋㅋㅋ
# 2k-1 완전 대칭 이동 12321
# 2k 살짝 이동  123321
# 2k+1 완전 대칭 이동 +1 1234321