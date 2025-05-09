#백준 2739번 구구단
#2024.05.09
#브론즈 5 
#포멧팅을 신경쓰자.
N = int(input())
for i in range (1,10):
    print("%d * %d = %d" %( N, i, N * i))