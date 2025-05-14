#2025.05.14
#s5 실버 달아버려서 그냥 실버 문제 드가본다 ㅋ
#다리 짓기 적합한 곳 == 사이트
#서쪽에 n, 동쪽에 m 다리는 못겹쳐짐..
def combination(n, r):
    result = 1
    for i in range(1, r+1):
        result = result * (n-i+1)//i #재귀
    return result


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(combination(M,N))
