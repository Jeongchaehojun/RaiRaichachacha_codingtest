#2025.10.30
#s2
from itertools import combinations

while True:
    data = list(map(int, input().split()))
    k = data[0]
    if k == 0:
        break
    S = data[1:]
    
    for combo in combinations(S, 6):
        print(*combo)
    print()  # 빈칸
