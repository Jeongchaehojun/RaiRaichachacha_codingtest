#2025.05.11
#bronze 5
N, X = map(int, input().split())
A = list(map(int, input().split()))
for num in A:
    if num < X:
        print(num, end = ' ')
#for num in A: 이렇게하면 리스트를 하나씩 인덱스..