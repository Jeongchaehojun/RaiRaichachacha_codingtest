#2025.09.20
#s3
#큐
from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split()))) #문서 중요도 저장
    order = 0   #몇 번째로 출력인지 카운트

    while q:
        if q[0] == max(q): #현재 문서가 가장 중요도가 높다면
            order += 1
            q.popleft()
            if m == 0:
                print(order)
                break
            else:
                m -= 1
        else:
            q.append(q.popleft())
            if m == 0:
                m = len(q) - 1
            else:
                m -= 1 