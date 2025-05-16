#2025.05.16
#b5
#이 문제 팩토리얼은 0이 안주어짐
n = int(input())
result = 1
for i in range(1, n+1):
    result *= i
print(result)