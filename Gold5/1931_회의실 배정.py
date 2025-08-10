#2025.08.10
#g5
#그리디 알고리즘 문제 찾아서 푼거임
#시간표 만들기 -> 그리디라고 생각하기
n = int(input())
council = [] #회의들 저장

for _ in range(n):
    a, b = map(int, input().split())
    council.append((a,b)) # 이렇게까지가 입력 처리


#정렬하는데,, 1차 기준은 종료시간이 빠른 순, 2차 기준은 종료 시간이 같을 때 시작 시간 기준
council.sort(key=lambda x: (x[1], x[0])) 

cnt = 0 #선택한 회의 개수
finish_time = 0 #현재 종료 시각

for s, f in council:
    if s >= finish_time: #정렬을 이미 위에서 했으니까 이때부터 그리디
        cnt += 1
        finish_time = f

print(cnt)