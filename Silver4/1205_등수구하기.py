#2025.07.14
#s4
N, S, P = map(int, input().split())

if N > 0:
    scores = list(map(int, input().split()))
else:
    scores = []

scores.append(S)
scores.sort(reverse=True)

rank = scores.index(S) + 1

if N == P and scores[P-1] > S:
    print(-1)
else:
    print(rank)
