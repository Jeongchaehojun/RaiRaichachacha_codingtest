#2025.07.17
#s4
#평행사변형 구하는건데 수식이 즐라 어려워서 힘을 빌림
import sys
import math

x1, y1, x2, y2, x3, y3 = map(int, sys.stdin.readline().split())

A = (x1, y1)
B = (x2, y2)
C = (x3, y3)

#1. 기울기 비교 (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2)
# 근데 분모가 0이 되는 경우가 있어서 곱하기로 비교해야 한대
# (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1)
if (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
    print(-1.0)
else: #2. 세 변의 길이
    dist_ab = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    dist_bc = math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)
    dist_ac = math.sqrt((A[0] - C[0])**2 + (A[1] - C[1])**2)

    #3. 가능한 둘레
    meter1 = 2*(dist_ab + dist_ac)
    meter2 = 2*(dist_ab + dist_bc)
    meter3 = 2*(dist_ac + dist_bc)

    #4. 최대 최소 찾기
    meters = [meter1, meter2, meter3]

    max_meter = max(meters)
    min_meter = min(meters)

    print(max_meter - min_meter)