#2025.08.07
#g5
#비트 마스킹 문제인데 비트연산일 뿐 비트 마스킹은 아님
#두 개의 병을 합친다는 것 자체가 이진수 연산
n, k = map(int, input().split())
result = 0

while bin(n).count('1') > k: #n을 이진수로 바꿔서 1의 개수를 센다. 
    idx = bin(n)[::-1].index('1') #이진수를 뒤집어서 가장 낮은 자리의 1의 위치 1100 -> 0011로 바뀌면 2번째임 (0,1,2)
    add = (1 << idx) #2의 idx승
    n += add #n에 add를 더해서 병을 새로 삼
    result += add #병 추가한 개수도 같이 누적
print(result)