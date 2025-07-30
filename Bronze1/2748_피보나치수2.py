#2025.07.30
#b1
#피보나치수는 dp 방식으로.
#메모이제이션
n = int(input())

fib = [0,1] #초기화

for i in range(2, n+1):
    fib.append(fib[i-1] + fib[i-2])

print(fib[n])