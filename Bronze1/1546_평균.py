#2025.05.22
#b1
N = int(input())
lst = list(map(int, input().split()))
M = max(lst)
hap = 0
for i in lst:
    hap += i/M*100
print(hap/N)