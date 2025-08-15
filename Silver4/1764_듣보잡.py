#2025.08.15
#s4
N, M = map(int, input().split())

dd = set()
for _ in range(N):
    dd.add(input().strip())

bd = set()
for _ in range(M):
    bd.add(input().strip())

ddbd = sorted(list(dd&bd))

print(len(ddbd))
for name in ddbd:
    print(name)