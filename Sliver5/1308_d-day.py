#2025.07.26
#s5
from datetime import date #이게 핵심ㅋㅋㅋ

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split()) # 목표

start = date(y1, m1, d1)
end = date(y2, m2, d2)

#limit = date(y1+1000, m1, d1) #일천년 한계 #런타임 에러 발생

if y2 > y1+1000 or (y2 == y1+1000 and (m2 > m1 or (m2 == m1 and d2 >= d1))):
    print('gg')

else:
    days = (end-start).days #일수만 뽑아냄. .days
    print(f"D-{days}")