#2025.09.06
#s5
#Greedy
S = int(input())

sum_num = 0
num = 1
cnt = 0

while sum_num + num <= S:
    sum_num += num
    num += 1
    cnt += 1
print(cnt)