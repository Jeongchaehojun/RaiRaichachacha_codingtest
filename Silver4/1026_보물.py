#2025.07.06
#s4
N = int(input())
A = sorted(map(int, input().split())) #오름차순
B = sorted(map(int, input().split()), reverse=True) #내림차순

print(sum(a * b for a, b in zip(A,B))) #zip은 같은 인덱스 값을 묶어서 곱
