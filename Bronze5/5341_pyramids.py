#2025.05.10
#bronze 5
import sys
for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    else:
        print(n *(n+1)//2)
# 피라미드 같이 1부터 n까지 수를 더하는 수식은 n * (n+1) // 2입니다!!