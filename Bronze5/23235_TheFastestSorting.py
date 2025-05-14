#2025.05.14
#b5
#제목은 가장 빠른 소팅 알고리즘인데 사실 소팅은 하지 않습니다.
import sys
linecount = 1
for line in sys.stdin:
    N = list(map(int, line.strip().split()))
    if(N[0]==0):
        break
    else:
        print(f"Case {linecount}: Sorting... done!")
        linecount +=1

#맞았드아!