#2025.09.07 
#s3
#greedy
import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split())) #길의 길이
price = list(map(int, input().split())) #기름의 가격

total = price[0] * L[0]
min_price = price[0] #가장 싼 주유 가격 초기화

for i in range(1, N-1):
    min_price = min(min_price, price[i]) # 더 저렴한 가격마다 갱신
    total += min_price * L[i]
print(total)