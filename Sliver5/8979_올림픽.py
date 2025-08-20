#2025.08.20
#s5
#대기업 기출문제
N, K = map(int, input().split())
countries = [] #나라들
for _ in range(N):
    countries.append(list(map(int, input().split())))

gold, silver, bronze = 0, 0, 0 #K의 메달
for country in countries:
    if country[0] == K:
        gold, silver, bronze = country[1], country[2], country[3]
        break

#K보다 순위가 높은 국가의 수
rnk = 1
for country in countries:
    gold2, silver2, bronze2 = country[1], country[2], country[3]

    if (gold2>gold) or (gold2 == gold and silver2 > silver) or (gold2 == gold and silver2 == silver and bronze2 > bronze):
        rnk += 1
print(rnk)