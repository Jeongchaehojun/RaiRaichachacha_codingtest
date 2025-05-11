#2025.05.11
#bronze 5
total = []
for _ in range(3):
    total.append(int(input().strip()))
total.sort() #append()로 리스트를 만든 다음에 정렬을 해야 1번 인덱스임!
print(total[1])

