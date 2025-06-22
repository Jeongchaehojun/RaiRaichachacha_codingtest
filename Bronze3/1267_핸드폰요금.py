#2025.06.23
#b3
n = int(input())  # 통화 개수
times = list(map(int, input().split()))  # 각 통화 시간 리스트

y_total = 0
m_total = 0

for t in times:
    y_total += ((t // 30) + 1) * 10
    m_total += ((t // 60) + 1) * 15

if y_total < m_total:
    print(f"Y {y_total}")
elif m_total < y_total:
    print(f"M {m_total}")
else:
    print(f"Y M {y_total}")
