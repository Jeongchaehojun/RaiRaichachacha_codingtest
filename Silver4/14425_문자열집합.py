#2025.10.02
#s4
n, m = map(int, input().split())
s = set(input().strip() for _ in range(n))
cnt = sum(1 for _ in range(m) if input().strip() in s)
print(cnt)