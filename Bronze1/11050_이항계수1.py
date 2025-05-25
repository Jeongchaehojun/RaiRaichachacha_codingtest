#2025.05.25
#b1
def combination(n, r):
    result = 1
    for i in range(1, r+1):
        result = result * (n-i+1)//i #재귀
    return result
N, K = map(int,input().split())
print(combination(N,K))