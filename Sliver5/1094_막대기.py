#2025.07.04
#s5
X = int(input())
count = 0

while X > 0:
    if X % 2 == 1:  # 이진수로 표현했을 때 1인 비트 수 세기
        count += 1
    X //= 2

print(count)
