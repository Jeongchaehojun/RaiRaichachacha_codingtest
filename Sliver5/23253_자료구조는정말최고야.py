#2025.09.10
#s5
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ok = True
for _ in range(M):
    k = int(input())
    book = list(map(int, input().split()))
#내림차순
    for i in range(k-1):
        if book[i] < book[i+1]:
            ok = False
            break
print("Yes" if ok else "No")