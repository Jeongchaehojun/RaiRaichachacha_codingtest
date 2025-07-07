
#2025.07.07
#s4
#그리디 알고리즘
#오사카에서 푸는데 공부할 겸 주석 철저.

# 줄 개수랑 브랜드 
need, brand = map(int, input().split())

# 세트 가격들, 낱개 가격들
setlist = []
onelist = []


for _ in range(brand):
    s, o = map(int, input().split())
    setlist.append(s)
    onelist.append(o)

# 제일 싼 세트, 낱개
setcheapest = min(setlist)
onecheapest = min(onelist)

# 경우 1: 세트만 사기 (남아도 어쩔 수 없음)
case1 = ((need // 6) + 1) * setcheapest

# 경우 2: 세트 몇 개 + 낱개로 나머지 채우기
case2 = (need // 6) * setcheapest + (need % 6) * onecheapest

# 경우 3: 전부 낱개로 사기
case3 = need * onecheapest

print(min(case1, case2, case3))
