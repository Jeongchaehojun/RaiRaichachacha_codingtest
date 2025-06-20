#2025.06.20
#s3
# 시험 월화수목금 찢음 ㅋㅋㅋㅋㅋㅋㅋ 개힘들다 
# 소수 구하기 문제.
m, n = map(int, input().split())

is_prime = [True] * (n+1)

is_prime[0] = False
is_prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]: #i가 아직 소수
        for j in range(i*i, n+1, i): #i의 배수는 전부 소수가 아님 i*i부터
            #왜냐 그 이전은 전부 지워짐 #에라토스테네스의 체?
            is_prime[j] = False

for i in range(m, n+1): #m부터 n까지 소수인 것만 출력
    if is_prime[i]:
        print(i)