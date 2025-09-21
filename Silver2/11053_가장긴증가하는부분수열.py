#2025.09.21
#s2
#dp
n = int(input())
a = list(map(int, input().split()))
d = [1] * n   #각 위치에서의 가장 긴 증가하는 부분 수열 길이 저장
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:   #증가하는 부분 수열
            d[i] = max(d[i], d[j] + 1)  
print(max(d))     