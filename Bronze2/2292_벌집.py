#2025.05.20
#b2
#1번 - 1개, 2번 - 6개, 3번 - 12개, 4번 - 18개
#규칙: 1번 제외 6의 배수
N = int(input())
#이항정리 6의 0배, 1배, 2배,,,
#(n*(n-1)/2) * 6 + 1 //원래는 n(n+1)/2 인데, 벌집에서 n 층에는 6*(n-1)입니다.
layer = 1
value = 1

while value <N:
    value += 6 *layer
    layer += 1
print(layer)