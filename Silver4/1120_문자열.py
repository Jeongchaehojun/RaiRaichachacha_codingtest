#2025.07.12
#s4
#문자열 A를 문자열 b에 겹치게 넣을 때, 다른 문자의 개수가 최소가 되도록하는 최솟값.
A, B = input().split() #문자열 입력이라서 map을 안써도 됨 ㄷㄷ
min = len(A)

for i in range(len(B) - len(A) + 1):
    diff = 0 #차이
    for j in range(len(A)):
        if A[j] != B[i + j]:
            diff += 1
    if diff < min:
        min = diff
print(min)

