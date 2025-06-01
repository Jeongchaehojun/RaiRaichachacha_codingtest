#2025.06.01
#s5
#이게 초딩 정보올림피아드인게 열이 받네

N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
rank = []

for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue
        if people[j][0] > people[i][0] and people[j][1]>people[i][1]:
            count +=1
    rank.append(count + 1)
print(*rank)

"""
튜플에 몸무게, 키가 등장하고
0번째요소(몸무게), 1번째요소(키)를 비교해서 둘 다 크면 count가 증가한다
덩치가 큰 사람을 세는 것이다.
등수 = 덩치 큰 사람 수 + 1
*rank는 랭크 리스트의 값을 공백을 가지고 한 줄로 출력해준다.
"""