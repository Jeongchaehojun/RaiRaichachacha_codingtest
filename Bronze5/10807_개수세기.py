#2025.05.11
#bronze 5
N = int(input())
numbers = list(map(int, input().split()))
v = int(input())

count = numbers.count(v) # .count()라는 메서드를 활용할 수 있따
print(count)
