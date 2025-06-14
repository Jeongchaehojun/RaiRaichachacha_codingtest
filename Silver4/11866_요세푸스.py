#2025.06.14
#s4
#요세푸스. k-1번 앞 요소 뒤로 보내기 
#근데 제거한 수들을 수열로 나열한거임
from collections import deque

n, k = map(int, input().split())
deq = deque(range(1,n+1))
result = []

while deq:
    deq.rotate(-(k-1)) #앞에서 k-1명 뒤로 보내기
    result.append(deq.popleft()) #k번째 사람 제거하기

print("<" + ", ".join(map(str,result)) + ">")