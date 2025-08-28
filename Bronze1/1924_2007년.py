
#2025.08.28
#b1
mm, dd= map(int, input().split())

lastdd= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

yoil = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

# 입력한 날짜까지 지난 날 계산
total_days = sum(lastdd[:mm- 1]) + dd - 1

print(yoil[total_days % 7])