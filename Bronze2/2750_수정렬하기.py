#2025.08.01
#b2
#정렬
n = int(input())


numbers = []


for _ in range(n):
    numbers.append(int(input()))


sorted_numbers = sorted(numbers)

for num in sorted_numbers:
    print(num)