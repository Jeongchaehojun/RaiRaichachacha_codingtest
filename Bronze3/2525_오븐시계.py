#2025.05.16
#b3
H, M = map(int, input().split())
pluselement = int(input())
total = H * 60 + M
plus = total + pluselement

if plus >= 24 * 60:
    plus -= 24*60
resultH = plus // 60
resultM = plus % 60
print(resultH, end=' ')
print(resultM)