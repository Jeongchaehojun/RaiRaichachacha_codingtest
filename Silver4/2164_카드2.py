#2025.06.04
#s4
""" N = int(input())
cards = list(range(1,N+1))

while len(cards)>1:
    cards.pop(0)
    cards.append(cards.pop(0))
print(cards[0]) """
#이거 시간복잡도 O(n)인데도 시간초과 남..
#수학적 접근: N이 2의 거듭제곱이면 마지막 = N, 아니면 마지막 = 2*(N-2^k)
#2^k는 N보다 작거나 같은 가장 큰 2의 거듭제곱

N = int(input())

power = 1
while power * 2 <= N:
    power *= 2
print(2*(N-power) if N != power else N)