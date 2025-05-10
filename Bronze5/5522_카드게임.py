#2025.05.10
#bronze 5
"""
import sys
sum = 0 #누적합 할 때 초기화를 해야해!!!!!!!
for line in sys.stdin:
    n = int(line.strip())
    sum += n
    print(sum)
"""
# 위 코드는 5줄만 받는게 아니라 EOF 입력 끝까지 받아버리고 배번 누적 값을 출력해서 틀림;;
# 걍 이거 외우셈 ㅋㅋㅋㅋㅋㅋ
total = 0
for _ in range(5):
    total += int(input().strip())
print(total)