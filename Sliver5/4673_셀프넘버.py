#2025.08.02
#s5
#브루트포싱 (완전탐색) 알고리즘 찾아서 시도하는 것입니다.
#셀프넘버는 해당 n과 n의 각자리수를 다 더한 수인 d(n)이 없는 수 입니다. 생성자가 없는 수
#d(n)은 무한 수열을 만들 수 있다고 함.
#이 문제는 입력은 없고 생성자가 없는 수인 셀프넘버를 10000이하로 한줄씩 출력
generated = set()
for i in range(1, 10001):
    n = i
    total = n
    for digit in str(n):
        total += int(digit) #여기까지가 total에다가 n을 넣고, n을 문자열로 바꿔서 각 자리수를 다시 정수로 바꿔서 total에 대입
    
    generated.add(total) #generated는 그렇게 생성된 숫자의 set

for i in range(1, 10001):
    if i not in generated: #1부터 반복해서 generated에 없으면?
        print(i)