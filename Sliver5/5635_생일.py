#2025.07.13
#s5
#메가커피에서 생일날 생일 문제 풀기
n = int(input())
people = []

for _ in range(n):
    name, d, m, y = input().split()
    people.append((int(y), int(m), int(d), name))

people.sort() 

print(people[-1][3])  # 가장 나이 적은 사람
print(people[0][3])   # 가장 나이 많은 사람
