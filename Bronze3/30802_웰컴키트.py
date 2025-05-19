#2025.05.19
#b3
N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())
tshirts = 0
for i in sizes:
    bundles = (i+ T - 1) //T
    tshirts += bundles
print(tshirts)

pen_bundles = N // P
pen = N % P
print(pen_bundles, pen)