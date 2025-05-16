#2025.05.16
#b5
N, A, B = map(int, input().split())
if B > A:
    print("Bus")
elif B == A:
    print("Anything")
else:
    print("Subway")