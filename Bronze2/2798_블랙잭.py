#2025.05.20
#b2
#nCr을 사용하려고 
"""
def combination(n,r):
    result = 1
    for i in range(1, r+1):
        result = result * (n - i + 1)//i
    return result
    
"""
from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
for comb in combinations(lst, 3):
    total = sum(comb)
    if total <= M and total > result:
        result = total

print(result)
