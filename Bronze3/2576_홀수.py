#2025.11.13
#b3
odd_numbers = []
for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        odd_numbers.append(n)

if odd_numbers:
    print(sum(odd_numbers))
    print(min(odd_numbers))
else:
    print(-1)
