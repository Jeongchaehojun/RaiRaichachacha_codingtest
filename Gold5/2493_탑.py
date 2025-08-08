#2025.08.08
#g5
#자료구조에 대한 문제. 
#stack임. 근데 이게 초등부 문제인게 레전드임ㅋㅋㅋㅋㅋㅋㅎㅋㅋㅋ

import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split())) #H = height

stack = [] # 지나온 탑들 (탑높이, 탑번호)
result = [0] * N # 0을 N개 만들어서 리스트 초기화

for i in range(N):
    now_h = H[i] #현재 탑 높이
    while stack and stack[-1][0] < now_h: #스택이 차있고, 스택의 마지막 top에 있는 탑이 현재보다 작으면 제거
        stack.pop()
    if stack:
        result[i] = stack[-1][1]
    else:
        result[i] = 0
    stack.append((now_h, i + 1)) #번호 1부터

print(*result)