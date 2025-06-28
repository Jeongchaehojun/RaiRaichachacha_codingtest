#2025.06.28
#b2
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a %= 10

    if a == 0:
        print(10)
    elif a in [1, 5, 6]:
        print(a)
    elif a in [4, 9]:
        cycle = 2
        b = b % cycle
        if b == 0:
            b = cycle
        result = (a ** b) % 10
        print(result)
    else:
        cycle = 4
        b = b % cycle
        if b == 0:
            b = cycle
        result = (a ** b) % 10
        print(result)
