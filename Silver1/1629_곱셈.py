#2025.10.14
#s1
#t1 ig
A, B, C = map(int, input().split())

def modmod(a, b, c):
    if b == 0:
        return 1
    half = modmod(a, b // 2, c)
    half = (half * half) % c
    if b % 2 == 1:
        half = (half * a) % c
    return half


print(modmod(A, B, C))
