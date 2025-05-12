#2025.05.12
#b5
#일본어로 되어있는 문제임
#근데 딱 봐도 a,e,i,o,u 모음이 영단어 중에 몇 개인지 보는거같음
#첫째줄에 영단어 길이 N, 둘째줄에 영단어 입력하면 그 중에 모음 출력되는듯
N = int(input())
Word = list(input().strip())
count = 0

for _ in range(N):
    if Word[_] in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print(count) #이 형식도 외워버리자.