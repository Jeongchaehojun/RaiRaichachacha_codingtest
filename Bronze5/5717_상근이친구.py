#2025.05.11
#bronze 5
import sys
for line in sys.stdin:
    M, F = map(int, line.strip().split()) #split()을 기억하자!!
    if(M == 0 and F == 0):
        break
    else:
        print(M+F)