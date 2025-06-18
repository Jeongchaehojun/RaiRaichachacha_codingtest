#2025.06.18
#s4
#오늘 알고리즘 시험이었는데 깜빡하고 이거 못풀뻔..ㄷㄷ
#알고리즘 시험은 개잘봤다ㅎ 물론 중간고사를 좀 말아먹긴..했는데ㅠ
import sys
input = sys.stdin.readline

def custom_round(x):
    return int(x + 0.5)  # 사사오입 반올림

n = int(input())
if n == 0:
    print(0)
else:
    scores = sorted([int(input()) for _ in range(n)])
    cut = custom_round(n * 0.15)  # 15% 자르기 (사사오입 반올림)
    trimmed = scores[cut : n - cut]  # 자르고 남은 값들
    avg = sum(trimmed) / len(trimmed)
    print(custom_round(avg))  # 평균도 사사오입 반올림

   
