#2025.10.31
#s5
score = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

total = 0   #학점*점수
ssum = 0  

for _ in range(20):
    name, hakjum, grade = input().split()
    hakjum = float(hakjum)
    if grade == "P":   # P는 계산 제외
        continue
    total += hakjum * score[grade]
    ssum += hakjum

print(f"{total / ssum}")
