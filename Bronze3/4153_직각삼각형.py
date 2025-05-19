#2025.05.19
#b3
import sys
for line in sys.stdin:
    byun = list(map(int, line.split())) #line().split() 해서 틀림 ㅋ
    if byun == [0, 0, 0]:
        break
    byun.sort()
    if (byun[0] **2 + byun[1]**2 == byun[2]**2):
        print("right")
    else:
        print("wrong")