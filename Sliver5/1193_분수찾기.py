#2025.10.12
#s5
#영어로 분모는 denominator, 분자는 numerator
n = int(input())

line = 1
while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    boonja = n
    boonmo = line - n + 1
else:
    boonja = line - n + 1
    boonmo = n

print(f"{boonja}/{boonmo}")