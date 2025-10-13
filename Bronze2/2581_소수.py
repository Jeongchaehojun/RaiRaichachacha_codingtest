def numbers2primes(M, N):
    primes = []
    for num in range(M, N + 1):
        if num > 1:  # 1은 소수 아님
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes #중요

M = int(input())
N = int(input())

primes = numbers2primes(M, N)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)