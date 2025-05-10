#백준 4101번
#2025.05.10
#브론즈 5
#입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 두 정수가 주어진다. 두 수는 백만보다 작거나 같은 양의 정수이다. 입력의 마지막 줄에는 0이 두 개 주어진다.

import sys
for line in sys.stdin:
    A, B = map(int, line.strip().split())
    if A==0 and B == 0: #문제에서 입력의 마지막에 0 0 이면 종료라고 써놓은거 숙지
        break
    if(A>B):
        print("Yes")
    else:
        print("No") #여기서 NO 둘 다 대문자로 적어서 틀렸었음

