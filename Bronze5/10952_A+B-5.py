#2025.05.11
#bronze 5
import sys
for line in sys.stdin:
    A, B = map(int, line.strip().split())
    if(A == 0 and B == 0):
        break
    else:
        print(A+B)
#와 진짜 이제 지린다; 진짜 다 내가 걍 자연스럽게 muscle memory