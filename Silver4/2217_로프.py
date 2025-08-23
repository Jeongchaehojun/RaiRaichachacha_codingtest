#2025.08.23
#s4
#greedy algorithm

N = int(input())
rope = [int(input()) for _ in range(N)] #각 로프가 버티는 최대 중량

rope.sort(reverse=True) #강한 로프부터 내림차순

max_weight = 0

for r, strength in enumerate(rope): #range 말고 enumerate 쓰면 0번부터 번호도 나옴
    max_weight = max(max_weight, strength * (r+1)) #r은 0부터라서.

print(max_weight)

#그리디 써서 그냥 가장 힘쎈 줄부터 추가해가면서 r개를 썼다는 것을 고려하면 되는 것이다.