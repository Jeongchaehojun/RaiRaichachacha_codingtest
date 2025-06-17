#2025.06.17
#s4
#오늘 운영체제 시험이라서 운영체제 비슷한 문제 찾음
# shortjobfirst sjf!!

import sys
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P.sort() # 가장 짧은 수행시간을 가지는 사람
wating_time = 0 # 각 프로세스의 반환시간
result = 0 # 전체 프로세스의 반환시간의 합
for i in P:
    wating_time += i
    result += wating_time

print(result)