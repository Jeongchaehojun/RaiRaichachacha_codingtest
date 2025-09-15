#2025.09.16
#s4
#에라토스테네스의체
N, K = map(int, input().split())
removed = [False] * (N + 1)
cnt = 0

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if not removed[j]:
            removed[j] = True
            cnt += 1
            if cnt == K:
                print(j)
                #raise SystemExit