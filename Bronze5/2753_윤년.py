#백준 2753번
#2025.05.09
#브론즈 5
yoon = int(input())
if(yoon%4==0 and yoon%100 != 0 or yoon%400==0):
    print(1)
else:
    print(0)