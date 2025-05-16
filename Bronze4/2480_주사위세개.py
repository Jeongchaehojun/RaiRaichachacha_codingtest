#2025.05.16
#b4
n1, n2, n3 = map(int, input().split())
lst = [n1, n2, n3]

if n1 == n2 == n3:
    n = 10000 + n1*1000
    print(n)
elif n1 == n2 or n1 == n3:
    n = 1000 + n1*100
    print(n)
elif n2 == n3:
    n = 1000 + n2*100
    print(n)
else:
    print(max(lst)*100)