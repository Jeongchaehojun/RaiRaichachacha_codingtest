#2025.10.01
#g5
# 2025.10.01
# g5

from collections import deque
import sys

input = sys.stdin.readline
data = input().splitlines()
t = int(data[0])
results = []

for i in range(1, t * 3, 3):
    commands = data[i]
    n = int(data[i + 1])
    
    # 배열 초기화
    if n > 0:
        # 배열이 비어있지 않다면, 대괄호를 제거하고 쉼표로 나눠 deque로 변환
        arr = deque(data[i + 2][1:-1].split(","))
    else:
        # 배열이 비어있다면 빈 deque 생성
        arr = deque()
    
    # 뒤집기 여부를 나타내는 플래그
    reverse = False
    
    # 에러 발생 여부를 나타내는 플래그
    error = False
    
    for command in commands:
        if command == 'R':
            # 뒤집기 명령어: reverse 플래그
            reverse = not reverse
        elif command == 'D':
            # 삭제 명령어
            if not arr:
                # 배열이 비어있으면 에러 처리
                results.append("error")
                error = True
                break
            if reverse:
                # 뒤집힌 상태라면 뒤에서 제거
                arr.pop()
            else:
                # 뒤집히지 않은 상태라면 앞에서 제거
                arr.popleft()
    
    # 에러가 발생하지 않았다면 결과 처리
    if not error:
        if reverse:
            # 최종적으로 뒤집힌 상태라면 배열을 뒤집음
            arr.reverse()
        # 배열을 문자열로 변환하여 결과에 추가
        results.append("[" + ",".join(arr) + "]")
sys.stdout.write("\n".join(results) + "\n")