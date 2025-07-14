#2025.07.14
#s4
N, S, P = map(int, input().split())
if N > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

rank = 1
for i in range(N):
    if scores[i] > S:
        rank += 1
    else:
        break

# 랭킹이 꽉 찼고, 내 점수가 꼴찌보다 작거나 같으면 못 들어감
if rank > P or (N==P and N>0 and S <= scores[N-1]):
    print(-1)
else:
    print(rank)

