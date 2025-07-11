#2025.07.11
#s4
L = int(input())
S = sorted(map(int, input().split()))
n = int(input())
#그리디 기반
if n in S:
    print(0)
else:
    # n보다 작은 수 중 가장 큰 수 (a), 없으면 0 
    #선형탐색
    a = 0
    for s in S:
        if s < n:
            a = s
        else:
            break
    
    # n보다 큰 수 중 가장 작은 수 (b), 없으면 마지막 수 + 1
    b = next((s for s in S if s > n), None)
    if b is None:
        b = n + 1

    
    print((n - a) * (b - n) - 1)
