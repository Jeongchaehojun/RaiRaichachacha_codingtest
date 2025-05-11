#2025.05.11
#브론즈 5
N, K = map(int, input().split())
bus = K
for i in range(N):
    A, B = map(int, input().split())
    bus += A
    bus -= B
print("비와이")
#이게 뭐냐 ㅋㅋㅋㅋ 개쓸데없는짓