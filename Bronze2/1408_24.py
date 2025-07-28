

# 2025.07.28
#b2
now = list(map(int, input().split(":")))
start = list(map(int, input().split(":")))

now_sec = now[0]*3600 + now[1]*60 + now[2]
start_sec = start[0]*3600 + start[1]*60 + start[2]

# 시간 차 계산 
if start_sec < now_sec:
    start_sec += 24 * 3600

diff = start_sec - now_sec

# 다시 시:분:초로 바꾸기
h = diff // 3600
m = (diff % 3600) // 60
s = diff % 60

print(f"{h:02d}:{m:02d}:{s:02d}")