#2025.05.30
#s5
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input().strip()))
sorted_lst = sorted(lst)
for num in sorted_lst:
    print(num)


#실버문제 치고는 easy