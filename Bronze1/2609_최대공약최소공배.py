#2025.05.23
#b1
#유클리드 호제법
a, b = map(int, input().split())

def gcd(x,y): #최대공약수임 #import math 쓰면 math.gcd(a,b)
    while y:
        x, y = y, x%y
    return x
g = gcd(a,b)
lcm = a*b//g

print(g)
print(lcm)