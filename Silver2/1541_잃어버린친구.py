#2025.08.16
#s2
#greedy algorithm
sik = input().strip() #주어진 식
parts = sik.split('-') #파츠
total = sum(map(int, parts[0].split('+')))

for segment in parts[1:]:
    total -= sum(map(int, segment.split('+')))

print(total)