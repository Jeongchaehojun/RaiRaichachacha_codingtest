#2025.11.11
#g4
#그리디 알고리즘
import heapq

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards) #가장 작은 카드 묶음부터 꺼내기 쉽다.

result = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += a + b

    heapq.heappush(cards, a + b)

print(result)