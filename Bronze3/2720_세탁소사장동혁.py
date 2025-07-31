#2025.07.31
#b3
T = int(input()) 

for _ in range(T):
    change = int(input())  # 거스름돈

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change  

    print(quarters, dimes, nickels, pennies)
