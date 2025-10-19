#2025.10.19
#b4
scores = [int(input()) for _ in range(5)] #입력을 받아버려
scores = [s if s >= 40 else 40 for s in scores] #40미만이면 40으로 바꿔버려
print(sum(scores) // 5)