#2025.05.19
#b2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

N = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in numbers:
    if is_prime(i):
        count +=1
print(count)