#2025.08.09
#s2
#스택 공부 더 하려고 했는데 문제를 이해하는 것부터 오래걸렸음
#1,2,3,4,5,6,7,8 이렇게 오름차순으로 계속 푸시하는 것이고 그래서 저 수열을 만들 수 있냐는 거
n = int(input())
stack = [] #스택
plusminus = [] # +, -
current = 1 #1부터 해서 계속 증가하며 스택에 넣어줘야함
possible = True #수열 생성 가능 여부

for _ in range(n):
    target = int(input()) #만들고 싶은 수 입력 들어오는거

    while current <= target:
        stack.append(current)
        plusminus.append('+')
        current += 1
    
    if stack[-1] == target:
        stack.pop()
        plusminus.append('-')
    else:
        possible = False
        break

if possible:
    print("\n".join(plusminus))
else:
    print("NO")