#2025.05.19
#b2
N = int(input())
for M in range(1, N):
    bunhae = sum(int(digit) for digit in  str(M))
    bunhaehap = M + bunhae
    if bunhaehap == N:
        print(M)
        break # 최소 찾고 바로 끝
else:
        print(0)