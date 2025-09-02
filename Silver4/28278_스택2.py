#2025.09.02
#s4
#stack problem yipnida

import sys
input = sys.stdin.readline #이거 없으니까 파이썬에서 또 시간초과남..;

X = int(input())
stack = []

for _ in range(X):
    cmd = input().split() #둘째줄부터 명령줌
    result = cmd[0]

    if result == '1': #X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
        stack.append(int(cmd[1])) 
    elif result == '2': #스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        print(stack.pop() if stack else -1)
    elif result == '3': # 스택에 들어있는 정수의 개수를 출력한다.
        print(len(stack))
    elif result == '4': #스택이 비어있으면 1, 아니면 0을 출력한다.
        print(0 if stack else 1)
    elif result == '5': #스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        print(stack[-1] if stack else -1) 