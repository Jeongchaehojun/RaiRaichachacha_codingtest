#2025.08.31
#b2
#greedy
taro = int(input().strip()) #타로가 지불한 돈
change = 1000 - taro #거스름돈
coins = [500, 100, 50, 10, 5, 1] #일본 돈인게 싹바가지가 없음
cnt = 0

for coin in coins:
    cnt += change // coin #현재 거스름돈을 해당 동전 단위로 몇 개 줄 수 있는지
    change %= coin #그렇게 나눈 다음 나머지 계속해서 보기
print(cnt)