#2025.05.16
#b3
H, M = map(int, input().split())
hour = H * 60
total = hour + M
minus45 = total - 45
if minus45<0:
    minus45 += 24 * 60
resultH = minus45//60 
resultM = minus45%60
print(resultH, end = ' ')
print(resultM)