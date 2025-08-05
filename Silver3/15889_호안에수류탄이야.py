#2025.08.05
#s3
#스위핑 문제 찾은건데 개재밌어보임 문제가
import sys
input = sys.stdin.readline

N = int(input().strip())
location = list(map(int, input().split()))
ranges = list(map(int, input().split()))

#여기서 윽제의 최대 도달 범위를 또 걸러주는게 히트임
now = location[0] + ranges[0] if N > 1 else location[0] #이 최대 설정이 중요 

for i in range(1, N):
    if location[i] > now:
        print("엄마 나 전역 늦어질 것 같아")
        break
    if i < N-1: #마지막 병사는 사거리 없음
        now = max(now, location[i] + ranges[i])
else:
    if now >= location[-1]:
        print("권병장님, 중대장님이 찾으십니다")
    else:
        print("엄마 나 전역 늦어질 것 같아")

