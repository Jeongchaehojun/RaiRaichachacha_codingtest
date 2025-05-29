#2025.05.29
#s5
import math
N = int(input())

num = str(math.factorial(N))
cnt = 0
for ch in reversed(num):
    if ch == '0':
        cnt += 1
    else:
        break
print(cnt)


"""
N = int(input())
cnt = 0
while N >= 5:
    N //= 5
    cnt += N
print(cnt)

"""
#이건 gpt추천인데 소인수 5로 몇 번나눌 수 있는지 결정. 5의 배수가 나올때마다 끝에 0이 하나씩 붙는다함..ㄷㄷ