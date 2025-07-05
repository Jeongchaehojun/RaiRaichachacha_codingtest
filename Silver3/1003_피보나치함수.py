#2025.07.05
#s3
T = int(input())
for _ in range(T):
    N = int(input())
    zero, one = 1, 0
    for i in range(N):
        zero, one = one, zero + one
    print(zero, one)