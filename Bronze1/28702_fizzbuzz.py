#2025.05.26
#b1
s = [input().strip() for _ in range(3)]

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
i = 1
while True:
    if [fizzbuzz(i), fizzbuzz(i+1), fizzbuzz(i+2)] == s:
        print(fizzbuzz(i+3))
        break