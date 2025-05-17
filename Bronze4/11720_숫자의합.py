#2025.05.17
#b4
T = int(input())
numbers = input().strip()
hap = 0
for i in range(T):
    hap += int(numbers[i])
print(hap)