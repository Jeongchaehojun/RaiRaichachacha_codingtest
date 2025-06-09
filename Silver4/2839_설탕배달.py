#2025.06.09
#s4
#그리디 알고리즘
def sugar(N):
    for five in range(N//5, -1, -1): #그리디 핵심. 줄여가기
        remain = N - five *5
        if remain % 3 == 0:
            return five + (remain//3)
    return -1
if __name__ == "__main__":
    N = int(input().strip())
    print(sugar(N))