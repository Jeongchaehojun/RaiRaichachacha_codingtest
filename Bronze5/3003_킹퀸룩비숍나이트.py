#백준3003번
#2025.05.09
#브론즈 5
kijun = [1, 1, 2, 2, 2, 8]
found= list(map(int, input().split()))
for k, f in zip(kijun, found): #기준에서 받은 수를 뺀 '차이',, zip()은 요소끼리 묶어 계산하는거
    print(k-f, end = ' ') #이거 공백이 중요해!!!!!!!
