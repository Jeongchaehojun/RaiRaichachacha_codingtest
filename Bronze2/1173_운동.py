#2025,06,09
#b2
N, m, M, T, R = map(int, input().split())

# 운동을 한 번도 못 하는 경우
if m + T > M:
    print(-1)
else:
    now = m        # 현재 심박수
    time = 0       # 전체 시간
    exercise = 0   # 운동한 시간

    while exercise < N:
        if now + T <= M:
            now += T
            exercise += 1
        else:
            now = max(m, now - R)
        time += 1

    print(time)