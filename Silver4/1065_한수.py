#2025.07.15
#s4
#한수라는 문제인데 한수란 양의 정수 x의 각 자리가 등차수열을 이루는 수임
#갠적으로 1이하 한수 개수가 1인것도 맘에 안듦 일단
#사실 한 자리, 두 자리는 모두 한수임;
N = int(input())
cnt = 0

if N < 100:
    cnt = N
else:
    cnt = 99
    for i in range(100, N+1):
        num = str(i) #일단 문자열로 바꿔야 각 자리로 접근 가능
        diff = int(num[0]) - int(num[1]) #등차를 저장해보기
        is_han = True
        
        for j in range(1, len(num)-1): #그 다음 자릿수부터 마지막 자리까지
            if int(num[j]) - int(num[j+1]) != diff: #아까 저장한 등차랑 다른지!!
                is_han = False #다르면 false 하고 런
                break
        if is_han:
            cnt += 1
print(cnt)