#2025.05.24
#b1
""" A, B ,V = map(int, input().split())
height = V
cnt = 0
days = 0
while True:
    cnt += A
    cnt -= B
    days += 1
    if cnt >= height:
        break
print(days) """ #이거 틀림 ㅆ
#마지막 날에는 미끌어지지 않는대.... math.ceil()로 정수 올림 사용
#V - B = 올라가야할 높이
#A - B = 하루에 올라간 높이
#days = (V-A)/(A-B)
import math
A, B ,V = map(int, input().split())
days = math.ceil((V-B)/(A-B)) #정수일수
print(days)