#2025.06.08
#b2
#시험 기간이라서 어려운 문제를 못풀겠음 걍..
#삼성 기출문제!
import math
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0

for students in A:
    total +=1 #총감독관 한 명 필수
    remain = students - B #총감독관이 커버한 후 남은 학생
    if remain > 0:
        total += math.ceil(remain/C) #남은학생수 / C을 올림하면 부감독관 수
print(total)

