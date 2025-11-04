#2025.11.4
#s3
import sys
input = sys.stdin.readline  

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    kind_cnt = {} # 종류가 개수가 됨 

    for _ in range(n):
        name, kind = input().split()

        if kind in kind_cnt:
            kind_cnt[kind] += 1
        else:
            kind_cnt[kind] = 1  

    result = 1
    for cnt in kind_cnt.values():
        result *= (cnt + 1) 
    result -= 1  # 아무것도 안입는 경우 제외
    print(result)