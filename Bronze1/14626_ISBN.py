#2025.06.13
#b1
numbers = input().rstrip()
total, index = 0, None # total: * 제외 합, index: *의 위치
for i, ch in enumerate(numbers[:-1]): #반복 가능한 개체 numbers에서 i는 몇 번째인지
                                #ch는 해당 위치에서 그 값
    if ch == '*':
        index = i #몇 번째에서 *이 있었는지 저장
    else:
        d = int(ch) #정수로 바꾸고
        total += d if i%2 == 0 else d*3 #짝수(i%2==0)면 그냥 누산하고 아니면 3곱해서 누산

m = int(numbers[-1]) #13번째 숫자

for x in range(10): # 그 * 위치에 숫자를 0부터 9까지 넣어보기
    weight = 1 if index%2 == 0 else 3
    tmp = total + x * weight
    #조건은 13자리 중에 마지막 자리 numbers[-1]는 그냥 더하기임
    #(12자리까지 가중치 써서 누적합 + 마지막 13번째 숫자)%10 == 0
    if(tmp + m)%10 == 0:
        print(x)
        break

