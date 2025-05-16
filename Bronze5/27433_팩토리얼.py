#2025.05.16
#b5
n=int(input())
result = 1
if n == 0:
    print("1")
else:
    for i in range(1, n+1): #range가n부터면 안됨
        result *= i
    print(result)
